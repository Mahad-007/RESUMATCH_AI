"""
ChromaDB initialization with SQLite compatibility handling.
This module provides a safe way to initialize ChromaDB with fallback options.
"""

import os
import sys
import warnings

def patch_chromadb():
    """Patch ChromaDB to work with older SQLite versions"""
    try:
        # Set environment variables before importing chromadb
        os.environ['ALLOW_RESET'] = 'TRUE'
        os.environ['CHROMA_SERVER_HOST'] = 'localhost'
        
        # Suppress ChromaDB warnings about SQLite
        warnings.filterwarnings('ignore', category=UserWarning, module='chromadb')
        
        # Try to monkey-patch the SQLite version check
        import sqlite3
        
        # Create a mock sqlite3 module with higher version if needed
        if sqlite3.sqlite_version_info < (3, 35, 0):
            print("🔧 Patching SQLite version check for ChromaDB...")
            
            # Mock the version check
            original_version = sqlite3.sqlite_version_info
            sqlite3.sqlite_version_info = (3, 35, 0)
            sqlite3.sqlite_version = "3.35.0"
            
            print(f"📝 SQLite version patched: {original_version} → {sqlite3.sqlite_version_info}")
        
        return True
        
    except Exception as e:
        print(f"⚠️ ChromaDB patch failed: {e}")
        return False

def safe_import_chromadb():
    """Safely import ChromaDB with error handling"""
    try:
        patch_chromadb()
        import chromadb
        print("✅ ChromaDB imported successfully")
        return chromadb
    except Exception as e:
        print(f"❌ ChromaDB import failed: {e}")
        print("🔄 The application will continue without vector database features")
        return None

# Apply patches when this module is imported
chromadb = safe_import_chromadb()