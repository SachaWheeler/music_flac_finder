import os
import numpy as np
import librosa
from mutagen.mp3 import MP3

def extract_audio_features(file_path):
    """Extract musical attributes from an MP3 file."""
    try:
        y, sr = librosa.load(file_path, sr=None, mono=True)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        chroma_stft = np.mean(librosa.feature.chroma_stft(y=y, sr=sr).T, axis=0)
        spectral_contrast = np.mean(librosa.feature.spectral_contrast(y=y, sr=sr).T, axis=0)
        return tempo, chroma_stft, spectral_contrast
    except Exception as e:
        print(f"Error extracting features from {file_path}: {e}")
        return None, None, None

def calculate_similarity(features1, features2):
    """Calculate similarity between two sets of audio features."""
    tempo1, chroma_stft1, spectral_contrast1 = features1
    tempo2, chroma_stft2, spectral_contrast2 = features2

    tempo_similarity = 1 - abs(tempo1 - tempo2) / max(tempo1, tempo2)
    chroma_similarity = np.dot(chroma_stft1, chroma_stft2) / (np.linalg.norm(chroma_stft1) * np.linalg.norm(chroma_stft2))
    spectral_similarity = np.dot(spectral_contrast1, spectral_contrast2) / (np.linalg.norm(spectral_contrast1) * np.linalg.norm(spectral_contrast2))

    return (tempo_similarity + chroma_similarity + spectral_similarity) / 3

def scan_directory(directory):
    """Scan a directory for MP3 files and return their audio features."""
    files_features = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mp3'):
                file_path = os.path.join(root, file)
                features = extract_audio_features(file_path)
                if all(features):
                    files_features.append((file_path, features))
    return files_features

def find_similar_files(target_features, directory_features):
    """Find and rank files similar to the target features."""
    similar_files = []

    for file_features in directory_features:
        file_path, features = file_features
        similarity_score = calculate_similarity(target_features, features)
        similar_files.append((file_path, similarity_score))

    similar_files.sort(key=lambda x: x[1], reverse=True)
    return similar_files

def main(target_file, directory_to_scan):
    """Main function to find similar MP3 files."""
    target_features = extract_audio_features(target_file)
    if not all(target_features):
        print(f"Failed to extract features from target file: {target_file}")
        return

    directory_features = scan_directory(directory_to_scan)
    similar_files = find_similar_files(target_features, directory_features)

    print(f"Files similar to {target_file}:")
    for file_path, score in similar_files:
        print(f"{file_path} (Similarity Score: {score:.2f})")

# Define the target MP3 file and the directory to scan
target_file = '/moshpit/Music/Music/Queens of the Stone Age/Songs For The Deaf/02 No One Knows.mp3'
directory_to_scan = '/moshpit/Music/Music/Tool'

# Run the main function
main(target_file, directory_to_scan)

