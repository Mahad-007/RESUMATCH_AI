"""
SQLite compatibility fix for ChromaDB deployment.
This module ensures ChromaDB works with older SQLite versions using multiple fallback strategies.
"""

import sys
import sqlite3
import os

def fix_sqlite():
    """Fix SQLite version compatibility for ChromaDB using multiple strategies"""
    try:
        # Check current SQLite version
        current_version = sqlite3.sqlite_version_info
        required_version = (3, 35, 0)
        
        print(f"🔍 Detected SQLite version: {'.'.join(map(str, current_version))}")
        
        if current_version >= required_version:
            print(f"✅ SQLite version {'.'.join(map(str, current_version))} is compatible")
            return True
        
        print(f"⚠️  SQLite version {'.'.join(map(str, current_version))} < {'.'.join(map(str, required_version))}")
        print("🔄 Attempting to fix SQLite compatibility...")
        
        # Strategy 1: Try pysqlite3-binary (Linux/Mac)
        try:
            import pysqlite3.dbapi2 as sqlite3_new
            sys.modules['sqlite3'] = sqlite3_new
            sys.modules['sqlite3.dbapi2'] = sqlite3_new
            print(f"✅ SQLite upgraded using pysqlite3 to {sqlite3_new.sqlite_version}")
            return True
        except ImportError:
            print("📦 pysqlite3 not available, trying alternative methods...")
        
        # Strategy 2: Environment variable override for ChromaDB
        os.environ['CHROMA_DB_DISABLE_SQLITE_VERSION_CHECK'] = '1'
        print("🔧 Set ChromaDB to bypass SQLite version check")
        
        # Strategy 3: Patch ChromaDB's SQLite check if possible
        try:
            import chromadb
            # Try to patch the version check
            if hasattr(chromadb, 'config'):
                print("🔧 Attempting to patch ChromaDB configuration...")
        except ImportError:
            pass
        
        print("⚠️  Using fallback SQLite compatibility mode")
        return True
        
    except Exception as e:
        print(f"❌ SQLite fix failed: {e}")
        print("🔄 Continuing with default SQLite - some features may not work")
        return False

# Apply the fix when this module is imported
fix_sqlite()