#!/usr/bin/env python3
"""
Run all 5 notebooks and collect hyperparameter sensitivity results
"""

import subprocess
import sys

notebooks = [
    '1_census_income.ipynb',
    '2_chronic_kidney_disease.ipynb',
    '3_energy_efficiency.ipynb',
    '4_thyroid_disease.ipynb',
    '5_wholesale_customers.ipynb'
]

print("="*80)
print("RUNNING ALL 5 NOTEBOOKS - HYPERPARAMETER SENSITIVITY ANALYSIS")
print("="*80)

for i, notebook in enumerate(notebooks, 1):
    print(f"\n[{i}/5] Executing: {notebook}")
    print("-"*80)
    
    try:
        result = subprocess.run(
            ['jupyter', 'nbconvert', '--to', 'notebook', '--execute', 
             '--inplace', '--ExecutePreprocessor.timeout=3600', notebook],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ {notebook} completed successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error executing {notebook}")
        print(f"Error: {e.stderr}")
        sys.exit(1)

print("\n" + "="*80)
print("✓ ALL NOTEBOOKS EXECUTED SUCCESSFULLY")
print("="*80)
print("\nResults saved to outputs/ directory")
