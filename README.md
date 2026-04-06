# Optimization Technique and Implementation Project Report (Part 1)

This folder contains the complete Part 1 deliverables for the HPC optimization assignment.

## Author Details

- Name: Sai Mohan Manukonda
- UC Student ID Number: 005046992

## Included Deliverables

### Required MS Files

1. `report/Part1_Optimization_Technique_Project_Report.docx`
   - Main project report (MS Word)
   - Includes optimization selection, analysis, empirical results, and references

2. `report/Part1_Source_Code_and_Screenshots.docx`
   - Source-code and screenshot evidence document (MS Word)
   - Includes implementation snippets and plot screenshots

3. `Part2_Elementary_Data_Structures_Presentation.pptx`
   - Part 2 presentation (MS PowerPoint)
   - Copied into this folder for centralized submission packaging

## Project Structure

- `src/`: baseline and optimized implementations
- `experiments/`: benchmark and plotting scripts
- `results/raw_data/`: CSV benchmark outputs
- `results/plots/`: generated result figures
- `report/`: Word report deliverables and generation utility

## Results and Reports

Quick links:

- Full results page: [results.md](results.md)
- Benchmark CSV: [results/raw_data/benchmark_results.csv](results/raw_data/benchmark_results.csv)
- Main report: [report/Part1_Optimization_Technique_Project_Report.docx](report/Part1_Optimization_Technique_Project_Report.docx)
- Source code and screenshots report: [report/Part1_Source_Code_and_Screenshots.docx](report/Part1_Source_Code_and_Screenshots.docx)

### Result Images

#### Speedup Summary

![Speedup Summary](results/plots/speedup_summary.png)

#### Timings by Distribution

![Timings by Distribution](results/plots/timings_by_distribution.png)

## How to Regenerate Artifacts

```bash
# from this folder
PYTHONPATH=. python experiments/run_benchmarks.py
python experiments/plot_results.py
python report/generate_ms_docs.py
```

## Notes

- The baseline deterministic quicksort intentionally demonstrates data-dependent vulnerability.
- The optimized variant demonstrates robust behavior across tested distributions.
- All generated artifacts are kept inside this folder for clean submission.
