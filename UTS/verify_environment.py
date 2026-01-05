import sys

print("="*70)
print("🔍 VERIFYING ENVIRONMENT FOR DRUG CONSUMPTION PREDICTION PROJECT")
print("="*70)

# ============================================
# CHECK PYTHON VERSION
# ============================================
print("\n1️⃣ Python Version:")
print(f"   ✓ Python {sys.version}")
if sys.version_info >= (3, 8):
    print("   ✅ Python version OK (>= 3.8)")
else:
    print("   ❌ Python version too old! Need >= 3.8")

# ============================================
# CHECK REQUIRED LIBRARIES
# ============================================
print("\n2️⃣ Checking Required Libraries:")
print("-"*70)

required_packages = {
    'numpy': '1.24.0',
    'pandas': '2.0.0',
    'scipy': '1.11.0',
    'sklearn': '1.3.0',
    'imblearn': '0.11.0',
    'matplotlib': '3.7.0',
    'seaborn': '0.12.0',
    'shap': '0.42.0',
    'statsmodels': '0.14.0',
    'joblib': '1.3.0',
}

all_ok = True
for package, min_version in required_packages.items():
    try:
        if package == 'sklearn':
            import sklearn
            pkg = sklearn
            pkg_name = 'scikit-learn'
        elif package == 'imblearn':
            import imblearn
            pkg = imblearn
            pkg_name = 'imbalanced-learn'
        else:
            pkg = __import__(package)
            pkg_name = package
        
        version = pkg.__version__
        print(f"   ✅ {pkg_name:20s} v{version}")
        
    except ImportError:
        print(f"   ❌ {package:20s} NOT INSTALLED!")
        all_ok = False
    except AttributeError:
        print(f"   ⚠️  {package:20s} (version unknown)")

# ============================================
# CHECK JUPYTER
# ============================================
print("\n3️⃣ Jupyter Environment:")
try:
    import notebook
    print(f"   ✅ Jupyter Notebook v{notebook.__version__}")
except ImportError:
    print("   ❌ Jupyter Notebook NOT INSTALLED!")
    all_ok = False

# ============================================
# TEST CRITICAL FUNCTIONS
# ============================================
print("\n4️⃣ Testing Critical Functions:")
print("-"*70)

try:
    # Test RandomForest
    from sklearn.ensemble import RandomForestClassifier
    print("   ✅ RandomForestClassifier imported")
    
    # Test SMOTE
    from imblearn.over_sampling import SMOTE, ADASYN
    print("   ✅ SMOTE & ADASYN imported")
    
    # Test SHAP
    import shap
    print("   ✅ SHAP imported")
    
    # Test RandomizedSearchCV
    from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
    print("   ✅ RandomizedSearchCV & StratifiedKFold imported")
    
    # Test metrics
    from sklearn.metrics import (
        roc_auc_score, precision_recall_curve, 
        confusion_matrix, classification_report,
        cohen_kappa_score, matthews_corrcoef
    )
    print("   ✅ All evaluation metrics imported")
    
except ImportError as e:
    print(f"   ❌ Import error: {e}")
    all_ok = False

# ============================================
# CHECK FOLDER STRUCTURE
# ============================================
print("\n5️⃣ Checking Folder Structure:")
import os

folders = [
    'data/raw',
    'data/processed',
    'notebooks',
    'models',
    'results/figures',
    'results/metrics',
    'results/reports'
]

for folder in folders:
    exists = os.path.exists(folder)
    status = "✅" if exists else "❌"
    print(f"   {status} {folder}/")
    if not exists:
        all_ok = False

# ============================================
# FINAL STATUS
# ============================================
print("\n" + "="*70)
if all_ok:
    print("🎉 ENVIRONMENT READY! Semua dependencies OK!")
    print("="*70)
    print("\n📝 Next Steps:")
    print("   1. Run: python 00_Download_Dataset.py")
    print("   2. Open: notebooks/01_EDA_Preprocessing.ipynb")
    print("   3. Start your analysis! 🚀")
else:
    print("⚠️  ENVIRONMENT INCOMPLETE!")
    print("="*70)
    print("\n🔧 To fix:")
    print("   1. Install missing packages: pip install -r requirements.txt")
    print("   2. Create missing folders: mkdir -p data/raw data/processed ...")
    print("   3. Re-run this script")

print("\n" + "="*70)