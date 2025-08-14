import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Wedge
from matplotlib.collections import LineCollection
import matplotlib.patheffects as path_effects
import os

# Set style for publication-quality figures
plt.style.use('default')
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

# Create output directory if it doesn't exist
output_dir = "extremophile_cooling_diagrams"
os.makedirs(output_dir, exist_ok=True)

def save_and_close(filename):
    """Helper function to save figure and close it"""
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{filename}.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}.png")

# 1. Biofouling Problem Overview
fig, ax1 = plt.subplots(figsize=(12, 8))
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_title('Biofouling in Liquid Cooling Systems: The Problem', fontweight='bold', fontsize=14)

# Clean system
clean_box = FancyBboxPatch((0.5, 7), 3, 2, boxstyle="round,pad=0.1", 
                          facecolor='lightblue', edgecolor='blue', linewidth=2)
ax1.add_patch(clean_box)
ax1.text(2, 8, 'Clean System\nOptimal Performance\n• High Heat Transfer\n• Low Pressure Drop', 
         ha='center', va='center', fontweight='bold')

# Fouled system
fouled_box = FancyBboxPatch((6, 7), 3, 2, boxstyle="round,pad=0.1", 
                           facecolor='lightcoral', edgecolor='red', linewidth=2)
ax1.add_patch(fouled_box)
ax1.text(7.5, 8, 'Fouled System\nDegraded Performance\n• Reduced Efficiency\n• Increased Costs', 
         ha='center', va='center', fontweight='bold')

# Temperature zones
temp_zones = [
    ('Mesophilic Zone\n20-45°C', 2, 4.5, 'lightgreen', 'Rapid biofilm growth'),
    ('Thermophilic Zone\n45-80°C', 5, 4.5, 'yellow', 'Moderate growth'),
    ('Hyperthermophilic\n>80°C', 8, 4.5, 'orange', 'Extremophile domain')
]

for zone, x, y, color, desc in temp_zones:
    zone_circle = Circle((x, y), 0.8, facecolor=color, edgecolor='black', linewidth=1.5)
    ax1.add_patch(zone_circle)
    ax1.text(x, y+0.2, zone, ha='center', va='center', fontweight='bold', fontsize=9)
    ax1.text(x, y-0.3, desc, ha='center', va='center', fontsize=8, style='italic')

# Problem factors
factors_box = FancyBboxPatch((1, 1.5), 8, 1.5, boxstyle="round,pad=0.1", 
                            facecolor='lightyellow', edgecolor='orange', linewidth=2)
ax1.add_patch(factors_box)
ax1.text(5, 2.25, 'Contributing Factors:\n• Nutrient availability • Surface roughness • Flow conditions\n• Temperature gradients • pH levels • Dissolved oxygen', 
         ha='center', va='center', fontweight='bold')

# Add degradation arrow
degrade_arrow = FancyArrowPatch((3.5, 8), (6, 8), arrowstyle='->', 
                               mutation_scale=25, color='red', linewidth=3)
ax1.add_patch(degrade_arrow)
ax1.text(4.75, 8.5, 'Biofilm Formation', ha='center', fontweight='bold', color='red')

ax1.set_xticks([])
ax1.set_yticks([])
ax1.axis('off')
save_and_close("01_biofouling_problem_overview")

# 2. Microbial Transformation Timeline
fig, ax2 = plt.subplots(figsize=(14, 8))
ax2.set_xlim(0, 14)
ax2.set_ylim(0, 8)
ax2.set_title('Planktonic to Biofilm Transformation Process', fontweight='bold', fontsize=14)

# Timeline stages
stages = [
    ('Planktonic\nCells', 1.5, 6, 'lightblue', 'Free-floating\nmicroorganisms'),
    ('Adhesion', 4, 6, 'lightgreen', 'Initial surface\nattachment'),
    ('Colonization', 6.5, 6, 'yellow', 'Cell multiplication\n& EPS production'),
    ('Maturation', 9, 6, 'orange', 'Complex 3D\nstructure formation'),
    ('Dispersal', 11.5, 6, 'lightcoral', 'Release of new\nplanktonic cells')
]

# Draw timeline arrow
timeline_arrow = FancyArrowPatch((0.5, 3), (13, 3), arrowstyle='->', 
                                mutation_scale=20, color='black', linewidth=2)
ax2.add_patch(timeline_arrow)
ax2.text(7, 2.5, 'Time (Hours to Days)', ha='center', fontweight='bold')

# Time markers
time_points = ['0-4 hrs', '4-12 hrs', '12-24 hrs', '24-72 hrs', '72+ hrs']
x_positions = [1.5, 4, 6.5, 9, 11.5]

for i, (stage, x, y, color, desc) in enumerate(stages):
    # Stage box
    stage_box = FancyBboxPatch((x-0.8, y-0.6), 1.6, 1.2, boxstyle="round,pad=0.1", 
                              facecolor=color, edgecolor='black', linewidth=1.5)
    ax2.add_patch(stage_box)
    ax2.text(x, y, stage, ha='center', va='center', fontweight='bold')
    
    # Description below
    ax2.text(x, 4.5, desc, ha='center', va='center', fontsize=9, style='italic')
    
    # Time marker
    ax2.text(x, 3.5, time_points[i], ha='center', va='center', fontweight='bold', color='blue')
    
    # Connecting arrows (except last)
    if i < len(stages) - 1:
        connect_arrow = FancyArrowPatch((x+0.8, y), (x_positions[i+1]-0.8, y), 
                                       arrowstyle='->', mutation_scale=15, color='gray')
        ax2.add_patch(connect_arrow)

# Add biofilm thickness indicator
thickness_data = [0.1, 0.5, 2.0, 8.0, 15.0]
ax2_twin = ax2.twinx()
ax2_twin.plot(x_positions, thickness_data, 'ro-', linewidth=2, markersize=8, label='Biofilm Thickness')
ax2_twin.set_ylabel('Biofilm Thickness (μm)', color='red', fontweight='bold')
ax2_twin.tick_params(axis='y', labelcolor='red')
ax2_twin.set_ylim(0, 20)

ax2.set_xticks([])
ax2.set_yticks([])
ax2.axis('off')
save_and_close("02_microbial_transformation_timeline")

# 3. Treatment Methods Comparison
fig, ax3 = plt.subplots(figsize=(12, 10))

methods = ['Chemical\nBiocides', 'UV\nDisinfection', 'Thermal\nTreatment', 'Ultrasonic\nCleaning', 'Biological\nControl']
effectiveness = [85, 70, 90, 65, 75]
cost = [60, 40, 80, 45, 30]
environmental_impact = [90, 20, 70, 35, 15]  # Higher = worse impact
maintenance = [40, 60, 50, 70, 80]  # Higher = more maintenance required

x_pos = np.arange(len(methods))
width = 0.2

# Create grouped bar chart
bars1 = ax3.bar(x_pos - 1.5*width, effectiveness, width, label='Effectiveness (%)', 
                color='green', alpha=0.7)
bars2 = ax3.bar(x_pos - 0.5*width, cost, width, label='Relative Cost', 
                color='blue', alpha=0.7)
bars3 = ax3.bar(x_pos + 0.5*width, environmental_impact, width, label='Environmental Impact', 
                color='red', alpha=0.7)
bars4 = ax3.bar(x_pos + 1.5*width, maintenance, width, label='Maintenance Need', 
                color='orange', alpha=0.7)

ax3.set_xlabel('Treatment Methods', fontweight='bold')
ax3.set_ylabel('Score (0-100)', fontweight='bold')
ax3.set_title('Comparison of Biofouling Treatment Methods', fontweight='bold', fontsize=14)
ax3.set_xticks(x_pos)
ax3.set_xticklabels(methods, fontweight='bold')
ax3.legend(loc='upper right')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(0, 100)

# Add value labels on bars
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.0f}', ha='center', va='bottom', fontsize=8)

save_and_close("03_treatment_methods_comparison")

# 4. Extremophile Classification
fig, ax4 = plt.subplots(figsize=(14, 10))
ax4.set_xlim(0, 14)
ax4.set_ylim(0, 10)
ax4.set_title('Extremophile Classification for Cooling Applications', fontweight='bold', fontsize=14)

# Main classification boxes
classifications = [
    ('Thermophiles', 2, 8, 'orange', '45-80°C\nThermus aquaticus\nGeobacillus species'),
    ('Hyperthermophiles', 6, 8, 'red', '>80°C\nPyrococcus furiosus\nThermotoga maritima'),
    ('Psychrophiles', 10, 8, 'lightblue', '<15°C\nPsychrobacter species\nColwellia species'),
    ('Halophiles', 2, 5, 'pink', 'High salinity\nHalobacterium species\nDunaliella salina'),
    ('Acidophiles', 6, 5, 'yellow', 'pH <3\nAcidithiobacillus\nSulfolobus species'),
    ('Alkaliphiles', 10, 5, 'lightgreen', 'pH >9\nBacillus alcalophilus\nNatronobacterium'),
    ('Barophiles', 4, 2, 'purple', 'High pressure\nPiezophiles\nDeep-sea organisms'),
    ('Radiophiles', 8, 2, 'gray', 'High radiation\nDeinococcus radiodurans\nRubrobacter radiotolerans')
]

for name, x, y, color, details in classifications:
    class_box = FancyBboxPatch((x-1.2, y-0.8), 2.4, 1.6, boxstyle="round,pad=0.1", 
                              facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.7)
    ax4.add_patch(class_box)
    ax4.text(x, y+0.2, name, ha='center', va='center', fontweight='bold', fontsize=11)
    ax4.text(x, y-0.3, details, ha='center', va='center', fontsize=8)

# Add application arrows
app_arrows = [
    ((4, 7.5), (6, 6.5), 'High-temp cooling'),
    ((8, 7.5), (10, 6.5), 'Enzyme production'),
    ((6, 4.5), (4, 2.8), 'Biofilm control'),
    ((10, 4.5), (8, 2.8), 'System cleaning')
]

for (start, end, label) in app_arrows:
    arrow = FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=15, 
                           color='darkblue', linestyle='dashed', linewidth=1.5)
    ax4.add_patch(arrow)
    mid_x, mid_y = (start[0] + end[0])/2, (start[1] + end[1])/2
    ax4.text(mid_x, mid_y, label, ha='center', va='center', fontsize=8, 
             bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

ax4.set_xticks([])
ax4.set_yticks([])
ax4.axis('off')
save_and_close("04_extremophile_classification")

# 5. Bio-Centric Solutions Architecture
fig, ax5 = plt.subplots(figsize=(15, 10))
ax5.set_xlim(0, 15)
ax5.set_ylim(0, 10)
ax5.set_title('Bio-Centric Cooling System Architecture', fontweight='bold', fontsize=14)

# Main components
components = [
    ('Cooling Reservoir', 2, 8, 3, 1.2, 'lightblue', 'Primary fluid storage\nwith beneficial microbes'),
    ('Bio-Film Reactor', 7, 8, 3, 1.2, 'lightgreen', 'Controlled biofilm\ncultivation chamber'),
    ('Heat Exchanger', 12, 8, 2.5, 1.2, 'orange', 'Enhanced heat transfer\nwith bio-enhancement'),
    ('Enzyme Injection', 2, 5.5, 3, 1.2, 'yellow', 'Targeted enzyme\ndelivery system'),
    ('Monitoring System', 7, 5.5, 3, 1.2, 'lightcoral', 'Real-time biofouling\ndetection & control'),
    ('Waste Processing', 12, 5.5, 2.5, 1.2, 'lightgray', 'Biofilm waste\nrecycling unit'),
    ('Control Interface', 7, 3, 3, 1.2, 'lightcyan', 'Integrated system\nmanagement')
]

for name, x, y, w, h, color, desc in components:
    comp_box = FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.1", 
                             facecolor=color, edgecolor='black', linewidth=2)
    ax5.add_patch(comp_box)
    ax5.text(x, y+0.2, name, ha='center', va='center', fontweight='bold')
    ax5.text(x, y-0.2, desc, ha='center', va='center', fontsize=9, style='italic')

# Flow connections
connections = [
    ((3.5, 8), (5.5, 8), 'Flow'),
    ((8.5, 8), (10.5, 8), 'Heat'),
    ((2, 6.7), (2, 6.7), 'Monitor'),
    ((7, 6.7), (7, 6.7), 'Control'),
    ((12, 6.7), (12, 6.7), 'Waste'),
    ((7, 4.2), (7, 2), 'Central Control')
]

# Draw flow arrows
flow_arrows = [
    FancyArrowPatch((3.5, 8), (5.5, 8), arrowstyle='->', mutation_scale=20, 
                   color='blue', linewidth=2),
    FancyArrowPatch((8.5, 8), (10.5, 8), arrowstyle='->', mutation_scale=20, 
                   color='red', linewidth=2),
    FancyArrowPatch((7, 6.9), (7, 4.2), arrowstyle='<->', mutation_scale=20, 
                   color='green', linewidth=2),
    FancyArrowPatch((5, 5.5), (2, 7.5), arrowstyle='->', mutation_scale=15, 
                   color='purple', linewidth=1.5, linestyle='dashed'),
    FancyArrowPatch((10, 5.5), (12, 7.5), arrowstyle='->', mutation_scale=15, 
                   color='purple', linewidth=1.5, linestyle='dashed')
]

for arrow in flow_arrows:
    ax5.add_patch(arrow)

# Add performance metrics box
metrics_box = FancyBboxPatch((0.5, 0.5), 14, 1.5, boxstyle="round,pad=0.1", 
                            facecolor='lightyellow', edgecolor='orange', linewidth=2)
ax5.add_patch(metrics_box)
ax5.text(7.5, 1.25, 'Performance Targets:\n• 95% biofilm control efficiency • 30% reduction in chemical usage • 20% improvement in heat transfer\n• Automated monitoring & response • Sustainable operation >5 years', 
         ha='center', va='center', fontweight='bold')

ax5.set_xticks([])
ax5.set_yticks([])
ax5.axis('off')
save_and_close("05_bio_centric_solutions_architecture")

# 6. Environmental Operating Conditions
fig, (ax6a, ax6b) = plt.subplots(1, 2, figsize=(15, 6))

# Temperature vs Performance
temp_range = np.linspace(20, 100, 100)
conventional_perf = 100 * np.exp(-((temp_range - 25)**2) / (2 * 15**2))  # Drops off quickly
extremophile_perf = 80 + 20 * np.exp(-((temp_range - 75)**2) / (2 * 20**2))  # Better at high temp

ax6a.plot(temp_range, conventional_perf, 'b-', linewidth=3, label='Conventional Systems')
ax6a.plot(temp_range, extremophile_perf, 'r-', linewidth=3, label='Extremophile-Enhanced')
ax6a.set_xlabel('Temperature (°C)', fontweight='bold')
ax6a.set_ylabel('System Performance (%)', fontweight='bold')
ax6a.set_title('Temperature Operating Range', fontweight='bold')
ax6a.legend()
ax6a.grid(True, alpha=0.3)
ax6a.set_ylim(0, 120)

# Operating zones
ax6a.axvspan(20, 45, alpha=0.2, color='green', label='Mesophilic Zone')
ax6a.axvspan(45, 80, alpha=0.2, color='yellow', label='Thermophilic Zone')
ax6a.axvspan(80, 100, alpha=0.2, color='red', label='Hyperthermophilic Zone')

# pH vs Microbial Activity
ph_range = np.linspace(3, 11, 100)
activity_acidophile = 100 * np.exp(-((ph_range - 4)**2) / (2 * 1.5**2))
activity_neutrophile = 100 * np.exp(-((ph_range - 7)**2) / (2 * 1**2))
activity_alkaliphile = 100 * np.exp(-((ph_range - 9.5)**2) / (2 * 1.5**2))

ax6b.plot(ph_range, activity_acidophile, 'orange', linewidth=3, label='Acidophiles')
ax6b.plot(ph_range, activity_neutrophile, 'blue', linewidth=3, label='Neutrophiles')
ax6b.plot(ph_range, activity_alkaliphile, 'green', linewidth=3, label='Alkaliphiles')
ax6b.set_xlabel('pH Level', fontweight='bold')
ax6b.set_ylabel('Microbial Activity (%)', fontweight='bold')
ax6b.set_title('pH Tolerance Ranges', fontweight='bold')
ax6b.legend()
ax6b.grid(True, alpha=0.3)
ax6b.set_ylim(0, 120)

save_and_close("06_environmental_operating_conditions")

# 7. Implementation Challenges Matrix
fig, ax7 = plt.subplots(figsize=(12, 10))

challenges = ['Regulatory\nApproval', 'Containment\nSafety', 'Cost\nEffectiveness', 
              'Technical\nComplexity', 'Public\nAcceptance', 'Scalability', 
              'Maintenance\nRequirements', 'Performance\nReliability']

scales = ['Industrial\nData Centers', 'Commercial\nHVAC', 'Consumer\nElectronics', 
          'Automotive\nCooling', 'Aerospace\nApplications']

# Create difficulty matrix (1-5 scale, 5 = most challenging)
difficulty_matrix = np.array([
    [4, 5, 3, 4, 5, 3, 3, 4],  # Industrial Data Centers
    [3, 4, 4, 3, 4, 4, 4, 3],  # Commercial HVAC
    [2, 2, 5, 2, 3, 5, 5, 3],  # Consumer Electronics
    [3, 3, 3, 3, 3, 3, 3, 4],  # Automotive Cooling
    [5, 5, 2, 5, 4, 2, 4, 5]   # Aerospace Applications
])

im = ax7.imshow(difficulty_matrix, cmap='RdYlGn_r', aspect='auto', vmin=1, vmax=5)

# Set ticks and labels
ax7.set_xticks(np.arange(len(challenges)))
ax7.set_yticks(np.arange(len(scales)))
ax7.set_xticklabels(challenges, rotation=45, ha='right', fontweight='bold')
ax7.set_yticklabels(scales, fontweight='bold')

# Add colorbar
cbar = plt.colorbar(im, ax=ax7)
cbar.set_label('Implementation Difficulty', rotation=270, labelpad=15, fontweight='bold')
cbar.set_ticks([1, 2, 3, 4, 5])
cbar.set_ticklabels(['Low', 'Moderate', 'Medium', 'High', 'Critical'])

# Add text annotations
for i in range(len(scales)):
    for j in range(len(challenges)):
        text = ax7.text(j, i, difficulty_matrix[i, j], ha='center', va='center', 
                       fontweight='bold', fontsize=12, color='white' if difficulty_matrix[i, j] > 3 else 'black')

ax7.set_title('Implementation Challenges by Application Scale', fontweight='bold', fontsize=14, pad=20)

save_and_close("07_implementation_challenges_matrix")

# 8. System Performance Metrics
fig, (ax8a, ax8b, ax8c) = plt.subplots(1, 3, figsize=(18, 6))

# Efficiency improvement over time
months = np.arange(0, 25, 1)
baseline = np.ones_like(months) * 100
bio_enhanced = 100 + 15 * (1 - np.exp(-months/6)) - 2 * np.sin(months/3)  # Gradual improvement
conventional = 100 - 5 * months/12 + np.random.normal(0, 2, len(months))  # Degradation

ax8a.plot(months, baseline, 'k--', linewidth=2, label='Baseline Performance')
ax8a.plot(months, bio_enhanced, 'g-', linewidth=3, label='Bio-Enhanced System')
ax8a.plot(months, conventional, 'r-', linewidth=2, label='Conventional System')
ax8a.set_xlabel('Months of Operation', fontweight='bold')
ax8a.set_ylabel('Relative Performance (%)', fontweight='bold')
ax8a.set_title('Long-term Performance', fontweight='bold')
ax8a.legend()
ax8a.grid(True, alpha=0.3)
ax8a.set_ylim(80, 125)

# Cost comparison
categories = ['Initial\nInvestment', 'Operating\nCosts', 'Maintenance\nCosts', 
              'Energy\nSavings', 'Replacement\nCosts', 'Total 5-year\nCost']
conventional_costs = [100, 100, 100, 0, 100, 100]
bio_enhanced_costs = [150, 70, 80, -30, 50, 75]

x_pos = np.arange(len(categories))
width = 0.35

bars1 = ax8b.bar(x_pos - width/2, conventional_costs, width, label='Conventional', 
                 color='red', alpha=0.7)
bars2 = ax8b.bar(x_pos + width/2, bio_enhanced_costs, width, label='Bio-Enhanced', 
                 color='green', alpha=0.7)

ax8b.set_xlabel('Cost Categories', fontweight='bold')
ax8b.set_ylabel('Relative Cost (%)', fontweight='bold')
ax8b.set_title('Cost Analysis', fontweight='bold')
ax8b.set_xticks(x_pos)
ax8b.set_xticklabels(categories, rotation=45, ha='right')
ax8b.legend()
ax8b.grid(True, alpha=0.3)
ax8b.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

# Environmental impact
impact_categories = ['Chemical\nUsage', 'Water\nConsumption', 'Energy\nEfficiency', 
                    'Waste\nGeneration', 'Carbon\nFootprint']
conventional_impact = [100, 100, 100, 100, 100]
bio_enhanced_impact = [30, 85, 120, 40, 70]

x_pos = np.arange(len(impact_categories))
bars3 = ax8c.bar(x_pos, conventional_impact, alpha=0.7, label='Conventional', color='red')
bars4 = ax8c.bar(x_pos, bio_enhanced_impact, alpha=0.7, label='Bio-Enhanced', color='green')

ax8c.set_xlabel('Environmental Factors', fontweight='bold')
ax8c.set_ylabel('Impact Level (% of baseline)', fontweight='bold')
ax8c.set_title('Environmental Impact', fontweight='bold')
ax8c.set_xticks(x_pos)
ax8c.set_xticklabels(impact_categories, rotation=45, ha='right')
ax8c.legend()
ax8c.grid(True, alpha=0.3)

# Add improvement annotations
for i, (conv, bio) in enumerate(zip(conventional_impact, bio_enhanced_impact)):
    improvement = ((conv - bio) / conv) * 100
    if improvement > 0:
        ax8c.annotate(f'-{improvement:.0f}%', xy=(i, bio), xytext=(i, bio-15),
                     ha='center', va='center', fontweight='bold', color='green',
                     arrowprops=dict(arrowstyle='->', color='green'))

save_and_close("08_system_performance_metrics")

# 9. Regulatory Framework Timeline
fig, ax9 = plt.subplots(figsize=(16, 8))
ax9.set_xlim(0, 16)
ax9.set_ylim(0, 10)
ax9.set_title('Regulatory Approval & Implementation Timeline', fontweight='bold', fontsize=14)

# Timeline phases
phases = [
    ('Research &\nDevelopment', 1.5, 7, 2.5, 'lightblue', 'Years 1-3\n• Lab testing\n• Proof of concept\n• Safety studies'),
    ('Regulatory\nSubmission', 5, 7, 2.5, 'yellow', 'Years 2-4\n• EPA filing\n• FDA consultation\n• Safety documentation'),
    ('Pilot Testing', 8.5, 7, 2.5, 'lightgreen', 'Years 4-6\n• Small scale trials\n• Performance validation\n• Risk assessment'),
    ('Commercial\nApproval', 12, 7, 2.5, 'orange', 'Years 5-7\n• Full regulatory approval\n• Manufacturing permits\n• Market authorization'),
    ('Market\nDeployment', 14.5, 7, 2.5, 'lightcoral', 'Years 6-8\n• Commercial launch\n• Scale-up production\n• Market adoption')
]

# Draw phases
for name, x, y, width, color, details in phases:
    phase_box = FancyBboxPatch((x-width/2, y-1), width, 2, boxstyle="round,pad=0.1", 
                              facecolor=color, edgecolor='black', linewidth=2)
    ax9.add_patch(phase_box)
    ax9.text(x, y+0.3, name, ha='center', va='center', fontweight='bold')
    ax9.text(x, y-0.5, details, ha='center', va='center', fontsize=9)

# Timeline arrow
timeline_arrow = FancyArrowPatch((0.5, 4), (15.5, 4), arrowstyle='->', 
                                mutation_scale=20, color='black', linewidth=2)
ax9.add_patch(timeline_arrow)
ax9.text(8, 3.5, 'Implementation Timeline (Years)', ha='center', fontweight='bold')

# Add year markers
for i, year in enumerate(range(1, 9)):
    x_pos = 1 + i * 2
    ax9.plot([x_pos, x_pos], [3.8, 4.2], 'k-', linewidth=2)
    ax9.text(x_pos, 3.3, f'Year {year}', ha='center', fontweight='bold', fontsize=9)

# Add risk/complexity indicators
risk_levels = [
    (3, 5, 'Medium Risk', 'lightblue'),
    (6.5, 5, 'High Risk', 'yellow'),
    (10, 5, 'Medium Risk', 'lightgreen'),
    (13.5, 5, 'Low Risk', 'orange')
]

for x, y, risk, color in risk_levels:
    risk_circle = Circle((x, y), 0.3, facecolor=color, edgecolor='black', alpha=0.7)
    ax9.add_patch(risk_circle)
    ax9.text(x, y, risk, ha='center', va='center', fontsize=8, fontweight='bold')

# Add milestone markers
milestones = [
    (4, 2, 'Safety\nValidated'),
    (7, 2, 'Pilot\nSuccess'),
    (11, 2, 'Regulatory\nApproval'),
    (14, 2, 'Market\nReady')
]

for x, y, milestone in milestones:
    milestone_box = FancyBboxPatch((x-0.6, y-0.4), 1.2, 0.8, boxstyle="round,pad=0.05", 
                                  facecolor='lightgray', edgecolor='black', linewidth=1)
    ax9.add_patch(milestone_box)
    ax9.text(x, y, milestone, ha='center', va='center', fontweight='bold', fontsize=8)

ax9.set_xticks([])
ax9.set_yticks([])
ax9.axis('off')
save_and_close("09_regulatory_framework_timeline")

# 10. Case Study Comparison
fig, ax10 = plt.subplots(figsize=(14, 10))
ax10.set_xlim(0, 14)
ax10.set_ylim(0, 12)
ax10.set_title('Case Studies: Scale-Specific Implementation', fontweight='bold', fontsize=14)

# Case study boxes
case_studies = [
    ('Data Center\nCooling', 2, 9.5, 'lightblue', 
     '• 10MW facility\n• 24/7 operation\n• Critical reliability\n• High heat density'),
    ('HVAC Systems', 7, 9.5, 'lightgreen', 
     '• Commercial buildings\n• Seasonal operation\n• Moderate reliability\n• Variable load'),
    ('Consumer Electronics', 12, 9.5, 'lightyellow', 
     '• Personal devices\n• Intermittent use\n• Cost sensitive\n• Compact design'),
    ('Automotive', 2, 6, 'lightcoral', 
     '• Engine cooling\n• Variable conditions\n• Safety critical\n• Weight constraints'),
    ('Industrial Process', 7, 6, 'lightgray', 
     '• Manufacturing\n• Continuous operation\n• Chemical compatibility\n• High temperature'),
    ('Aerospace', 12, 6, 'orange', 
     '• Space applications\n• Extreme environments\n• Ultra-reliable\n• Minimal maintenance')
]

for name, x, y, color, details in case_studies:
    case_box = FancyBboxPatch((x-1.5, y-1.2), 3, 2.4, boxstyle="round,pad=0.1", 
                             facecolor=color, edgecolor='black', linewidth=2)
    ax10.add_patch(case_box)
    ax10.text(x, y+0.5, name, ha='center', va='center', fontweight='bold', fontsize=11)
    ax10.text(x, y-0.3, details, ha='center', va='center', fontsize=9)

# Implementation feasibility scores
feasibility_data = [
    ('Data Center', 85, 'High'),
    ('HVAC', 75, 'Medium-High'),
    ('Consumer', 45, 'Medium'),
    ('Automotive', 60, 'Medium'),
    ('Industrial', 90, 'High'),
    ('Aerospace', 35, 'Low-Medium')
]

# Add feasibility indicators
for i, (name, score, level) in enumerate(feasibility_data):
    x_positions = [2, 7, 12, 2, 7, 12]
    y_positions = [7.8, 7.8, 7.8, 4.3, 4.3, 4.3]
    
    # Color based on score
    if score >= 80:
        indicator_color = 'green'
    elif score >= 60:
        indicator_color = 'yellow'
    else:
        indicator_color = 'red'
    
    feasibility_circle = Circle((x_positions[i], y_positions[i]), 0.3, 
                               facecolor=indicator_color, edgecolor='black', alpha=0.8)
    ax10.add_patch(feasibility_circle)
    ax10.text(x_positions[i], y_positions[i], f'{score}%', ha='center', va='center', 
             fontweight='bold', fontsize=9, color='white' if score < 70 else 'black')

# Add summary comparison table
table_box = FancyBboxPatch((1, 1), 12, 2.5, boxstyle="round,pad=0.1", 
                          facecolor='lightcyan', edgecolor='blue', linewidth=2)
ax10.add_patch(table_box)

table_header = 'Implementation Summary:\n'
table_content = (
    'High Feasibility: Data Centers (85%), Industrial Process (90%) - Controlled environments, high value applications\n'
    'Medium Feasibility: HVAC (75%), Automotive (60%) - Moderate complexity, established infrastructure\n'
    'Lower Feasibility: Consumer Electronics (45%), Aerospace (35%) - Cost constraints, extreme requirements'
)

ax10.text(7, 2.5, table_header, ha='center', va='center', fontweight='bold', fontsize=12)
ax10.text(7, 1.8, table_content, ha='center', va='center', fontsize=10)

ax10.set_xticks([])
ax10.set_yticks([])
ax10.axis('off')
save_and_close("10_case_study_comparison")

print("\nExtremophile Liquid Cooling Systems Visualization Complete!")
print(f"\nAll PNG files saved to: {output_dir}/")
print("\nGenerated files:")
print("1. 01_biofouling_problem_overview.png")
print("2. 02_microbial_transformation_timeline.png") 
print("3. 03_treatment_methods_comparison.png")
print("4. 04_extremophile_classification.png")
print("5. 05_bio_centric_solutions_architecture.png")
print("6. 06_environmental_operating_conditions.png")
print("7. 07_implementation_challenges_matrix.png")
print("8. 08_system_performance_metrics.png")
print("9. 09_regulatory_framework_timeline.png")
print("10. 10_case_study_comparison.png")