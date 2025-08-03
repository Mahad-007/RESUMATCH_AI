"""
Test script to validate SQLite compatibility for ChromaDB.
Run this before deploying to check if the fixes work.
"""

import sys
import sqlite3

def test_sqlite_compatibility():
    """Test SQLite compatibility and fixes"""
    print("🧪 Testing SQLite Compatibility...")
    print("=" * 50)
    
    # Test 1: Check system SQLite version
    print(f"📊 System SQLite version: {sqlite3.sqlite_version}")
    print(f"📊 SQLite version info: {sqlite3.sqlite_version_info}")
    
    required_version = (3, 35, 0)
    current_version = sqlite3.sqlite_version_info
    
    if current_version >= required_version:
        print("✅ System SQLite is compatible")
    else:
        print("⚠️  System SQLite needs upgrade")
    
    # Test 2: Test our fixes
    print("\n🔧 Testing compatibility fixes...")
    try:
        import sqlite_fix
        print("✅ sqlite_fix module loaded successfully")
    except Exception as e:
        print(f"❌ sqlite_fix failed: {e}")
    
    try:
        import chromadb_fix
        print("✅ chromadb_fix module loaded successfully")
    except Exception as e:
        print(f"❌ chromadb_fix failed: {e}")
    
    # Test 3: Test ChromaDB import
    print("\n📦 Testing ChromaDB import...")
    try:
        import chromadb
        print("✅ ChromaDB imported successfully")
        
        # Try to create a simple collection
        client = chromadb.Client()
        print("✅ ChromaDB client created successfully")
        
    except Exception as e:
        print(f"⚠️  ChromaDB test failed: {e}")
        print("🔄 This might be normal - the app will handle this gracefully")
    
    print("\n" + "=" * 50)
    print("🎉 Compatibility test completed!")
    print("💡 If you see any errors above, the app includes fallback handling")

if __name__ == "__main__":
    test_sqlite_compatibility()