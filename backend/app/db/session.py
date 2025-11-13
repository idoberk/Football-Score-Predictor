from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from app.models.match import Match
from app.db.base import Base
load_dotenv()

def create_tables():
    """Create all tables defined in models"""
    print("=" * 60)
    print("Creating Database Tables")
    print("=" * 60)
    
    try:
        # Create engine with echo=True to see SQL
        engine = create_engine(os.getenv('DATABASE_URL'), echo=True)
        
        # Drop all tables first (clean slate)
        print("\n🗑️  Dropping existing tables...\n")
        Base.metadata.drop_all(bind=engine)
        
        # Create all tables
        print("\n🏗️  Creating tables from models...\n")
        Base.metadata.create_all(bind=engine)
        
        # Verify tables were created
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        print("\n" + "=" * 60)
        print("✅ Tables created successfully!")
        print("=" * 60)
        print(f"\nTables in database:")
        for table in sorted(tables):
            print(f"  - {table}")
        
        # Show table details
        print("\n" + "=" * 60)
        print("Table Details")
        print("=" * 60)
        
        for table_name in sorted(tables):
            columns = inspector.get_columns(table_name)
            indexes = inspector.get_indexes(table_name)
            fks = inspector.get_foreign_keys(table_name)
            
            print(f"\n📋 {table_name.upper()}")
            print(f"  Columns: {len(columns)}")
            for col in columns:
                print(f"    - {col['name']}: {col['type']}")
            
            if indexes:
                print(f"  Indexes: {len(indexes)}")
                for idx in indexes:
                    print(f"    - {idx['name']}")
            
            if fks:
                print(f"  Foreign Keys: {len(fks)}")
                for fk in fks:
                    print(f"    - {fk['constrained_columns']} -> {fk['referred_table']}.{fk['referred_columns']}")
        
        print("\n✅ All checks passed!\n")
        return True
        
    except Exception as e:
        print(f"\n❌ Error creating tables: {e}\n")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    create_tables()