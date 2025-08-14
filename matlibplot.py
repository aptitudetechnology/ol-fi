import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
from matplotlib.collections import LineCollection
import os

# Set style for publication-quality figures
plt.style.use('default')
plt.rcParams['font.size'] = 10

# Create output directory if it doesn't exist
output_dir = "bio_lifi_diagrams"
os.makedirs(output_dir, exist_ok=True)

def save_and_close(filename):
    """Helper function to save figure and close it"""
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{filename}.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}.png")

# 1. Bioluminescent Organism Mechanisms
fig, ax1 = plt.subplots(figsize=(12, 8))
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 8)
ax1.set_title('Bioluminescent Organism Control Mechanisms', fontweight='bold', fontsize=14)

# Quorum Sensing Pathway
qs_box = FancyBboxPatch((0.5, 6), 2, 1.2, boxstyle="round,pad=0.1", 
                        facecolor='lightblue', edgecolor='blue', linewidth=2)
ax1.add_patch(qs_box)
ax1.text(1.5, 6.6, 'Quorum\nSensing', ha='center', va='center', fontweight='bold')

# Stimulus-Driven Pathway
sd_box = FancyBboxPatch((4, 6), 2, 1.2, boxstyle="round,pad=0.1", 
                        facecolor='lightgreen', edgecolor='green', linewidth=2)
ax1.add_patch(sd_box)
ax1.text(5, 6.6, 'Stimulus\nDriven', ha='center', va='center', fontweight='bold')

# Neural Control
nc_box = FancyBboxPatch((7.5, 6), 2, 1.2, boxstyle="round,pad=0.1", 
                        facecolor='lightyellow', edgecolor='orange', linewidth=2)
ax1.add_patch(nc_box)
ax1.text(8.5, 6.6, 'Neural\nControl', ha='center', va='center', fontweight='bold')

# Gene Circuit
gc_box = FancyBboxPatch((4, 3.5), 2, 1.2, boxstyle="round,pad=0.1", 
                        facecolor='lightcoral', edgecolor='red', linewidth=2)
ax1.add_patch(gc_box)
ax1.text(5, 4.1, 'Gene\nCircuit', ha='center', va='center', fontweight='bold')

# Bioluminescence Output
bio_box = FancyBboxPatch((4, 1), 2, 1.2, boxstyle="round,pad=0.1", 
                         facecolor='gold', edgecolor='darkorange', linewidth=2)
ax1.add_patch(bio_box)
ax1.text(5, 1.6, 'Bioluminescent\nOutput', ha='center', va='center', fontweight='bold')

# Add arrows
arrows = [
    FancyArrowPatch((1.5, 6), (4.5, 4.5), arrowstyle='->', mutation_scale=20, color='blue'),
    FancyArrowPatch((5, 6), (5, 4.7), arrowstyle='->', mutation_scale=20, color='green'),
    FancyArrowPatch((8.5, 6), (5.5, 4.5), arrowstyle='->', mutation_scale=20, color='orange'),
    FancyArrowPatch((5, 3.5), (5, 2.2), arrowstyle='->', mutation_scale=20, color='red')
]
for arrow in arrows:
    ax1.add_patch(arrow)

ax1.set_xticks([])
ax1.set_yticks([])
ax1.axis('off')
save_and_close("01_bioluminescent_control_mechanisms")

# 2. Multi-Wavelength Transmission
fig, ax2 = plt.subplots(figsize=(10, 6))
wavelengths = ['Blue\n(475nm)', 'Green\n(510nm)', 'Yellow\n(575nm)', 'Red\n(650nm)']
intensities = [85, 92, 78, 88]
colors = ['blue', 'green', 'yellow', 'red']

bars = ax2.bar(wavelengths, intensities, color=colors, alpha=0.7, edgecolor='black')
ax2.set_ylabel('Signal Intensity (%)')
ax2.set_title('Multi-Wavelength Bio-LiFi Channels', fontweight='bold', fontsize=14)
ax2.set_ylim(0, 100)

# Add data labels
for bar, intensity in zip(bars, intensities):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
             f'{intensity}%', ha='center', va='bottom', fontweight='bold')

ax2.grid(True, alpha=0.3)
save_and_close("02_multi_wavelength_channels")

# 3. Retinal Layer Structure
fig, ax3 = plt.subplots(figsize=(12, 8))
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.set_title('Biological Photoreceptor Network Structure', fontweight='bold', fontsize=14)

# Draw retinal layers
layers = [
    ('Photoreceptors', 8, 'lightblue', 'Rods & Cones'),
    ('Horizontal Cells', 6.5, 'lightgreen', 'Lateral Processing'),
    ('Bipolar Cells', 5, 'lightyellow', 'Vertical Transmission'),
    ('Amacrine Cells', 3.5, 'lightcoral', 'Signal Modulation'),
    ('Ganglion Cells', 2, 'lightgray', 'Output Layer')
]

for name, y_pos, color, function in layers:
    layer_rect = Rectangle((1, y_pos-0.4), 8, 0.8, facecolor=color, 
                          edgecolor='black', linewidth=1)
    ax3.add_patch(layer_rect)
    ax3.text(2, y_pos, name, va='center', fontweight='bold')
    ax3.text(7, y_pos, function, va='center', style='italic')

# Add light input arrow
light_arrow = FancyArrowPatch((5, 9.5), (5, 8.4), arrowstyle='->', 
                             mutation_scale=25, color='gold', linewidth=3)
ax3.add_patch(light_arrow)
ax3.text(5, 9.7, 'Light Input', ha='center', fontweight='bold', color='gold')

# Add output arrow
output_arrow = FancyArrowPatch((5, 1.6), (5, 0.5), arrowstyle='->', 
                              mutation_scale=25, color='darkblue', linewidth=3)
ax3.add_patch(output_arrow)
ax3.text(5, 0.3, 'Neural Output', ha='center', fontweight='bold', color='darkblue')

ax3.set_xticks([])
ax3.set_yticks([])
ax3.axis('off')
save_and_close("03_photoreceptor_network_structure")

# 4. System Architecture
fig, ax4 = plt.subplots(figsize=(12, 8))
ax4.set_xlim(0, 12)
ax4.set_ylim(0, 10)
ax4.set_title('Bio-LiFi System Architecture', fontweight='bold', fontsize=14)

# Transmitter side
tx_box = FancyBboxPatch((0.5, 7), 3, 1.5, boxstyle="round,pad=0.1", 
                        facecolor='lightblue', edgecolor='blue', linewidth=2)
ax4.add_patch(tx_box)
ax4.text(2, 7.75, 'Biological\nTransmitter', ha='center', va='center', fontweight='bold')

# Channel
channel_box = FancyBboxPatch((4.5, 7), 3, 1.5, boxstyle="round,pad=0.1", 
                            facecolor='lightyellow', edgecolor='orange', linewidth=2)
ax4.add_patch(channel_box)
ax4.text(6, 7.75, 'Optical\nChannel', ha='center', va='center', fontweight='bold')

# Receiver side
rx_box = FancyBboxPatch((8.5, 7), 3, 1.5, boxstyle="round,pad=0.1", 
                        facecolor='lightgreen', edgecolor='green', linewidth=2)
ax4.add_patch(rx_box)
ax4.text(10, 7.75, 'Biological\nReceiver', ha='center', va='center', fontweight='bold')

# Processing layers
proc_layers = [
    ('Physical Layer', 5, 'lightcoral'),
    ('Data Link Layer', 3.5, 'lightgray'),
    ('Network Layer', 2, 'lightcyan')
]

for layer, y_pos, color in proc_layers:
    layer_rect = FancyBboxPatch((1, y_pos-0.4), 10, 0.8, boxstyle="round,pad=0.05", 
                               facecolor=color, edgecolor='black', linewidth=1)
    ax4.add_patch(layer_rect)
    ax4.text(6, y_pos, layer, ha='center', va='center', fontweight='bold')

# Add connection arrows
conn_arrows = [
    FancyArrowPatch((3.5, 7.75), (4.5, 7.75), arrowstyle='->', mutation_scale=20),
    FancyArrowPatch((7.5, 7.75), (8.5, 7.75), arrowstyle='->', mutation_scale=20)
]
for arrow in conn_arrows:
    ax4.add_patch(arrow)

ax4.set_xticks([])
ax4.set_yticks([])
ax4.axis('off')
save_and_close("04_system_architecture")

# 5. Signal Transduction Pathway
fig, ax5 = plt.subplots(figsize=(10, 10))
ax5.set_xlim(0, 10)
ax5.set_ylim(0, 12)
ax5.set_title('Signal Transduction Timeline', fontweight='bold', fontsize=14)

# Timeline steps
steps = [
    ('Photon Absorption', 10, 0),
    ('Rhodopsin Activation', 8.5, 50),
    ('G-protein Cascade', 7, 150),
    ('Ion Channel Response', 5.5, 300),
    ('Membrane Potential Change', 4, 500),
    ('Neurotransmitter Release', 2.5, 800),
    ('Neural Signal Generation', 1, 1200)
]

times = [step[2] for step in steps]
y_positions = [step[1] for step in steps]
labels = [step[0] for step in steps]

# Draw timeline
ax5.plot([0, 0], [0.5, 11], 'k-', linewidth=3)
for i, (label, y_pos, time) in enumerate(steps):
    # Time marker
    ax5.plot([0, 1], [y_pos, y_pos], 'k-', linewidth=2)
    ax5.text(1.5, y_pos, f'{label}', va='center', fontweight='bold')
    ax5.text(8, y_pos, f'{time} μs', va='center', ha='right', style='italic')
    
    # Add process box
    proc_box = FancyBboxPatch((2, y_pos-0.3), 4, 0.6, boxstyle="round,pad=0.05", 
                             facecolor=plt.cm.viridis(i/len(steps)), alpha=0.7,
                             edgecolor='black', linewidth=1)
    ax5.add_patch(proc_box)

ax5.text(-0.5, 6, 'Time →', rotation=90, ha='center', va='center', fontweight='bold')
ax5.set_xticks([])
ax5.set_yticks([])
ax5.axis('off')
save_and_close("05_signal_transduction_timeline")

# 6. Event-Driven Communication
fig, ax6 = plt.subplots(figsize=(12, 6))
t = np.linspace(0, 10, 1000)
# Generate spike train data
spike_times = [1, 1.5, 2.8, 3.2, 4.5, 5.1, 6.7, 7.2, 8.8, 9.5]
spike_signal = np.zeros_like(t)
for spike_time in spike_times:
    spike_idx = np.argmin(np.abs(t - spike_time))
    spike_signal[spike_idx:spike_idx+10] = 1

ax6.plot(t, spike_signal, 'b-', linewidth=2, label='Bioluminescent Pulses')
ax6.fill_between(t, 0, spike_signal, alpha=0.3, color='blue')
ax6.set_xlabel('Time (seconds)')
ax6.set_ylabel('Signal Intensity')
ax6.set_title('Event-Driven Bio-LiFi Communication', fontweight='bold', fontsize=14)
ax6.set_ylim(-0.1, 1.2)
ax6.grid(True, alpha=0.3)
ax6.legend()

# Add data encoding annotation
ax6.text(2, 1.1, 'Data: 101101', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7),
         fontweight='bold', ha='center')
save_and_close("06_event_driven_communication")

# 7. Environmental Sensitivity
fig, ax7 = plt.subplots(figsize=(12, 6))
temp_range = np.linspace(15, 35, 100)
intensity_temp = 100 * np.exp(-((temp_range - 25)**2) / (2 * 5**2))  # Gaussian around 25°C

salinity_range = np.linspace(0, 40, 100)
intensity_sal = 100 * np.exp(-((salinity_range - 35)**2) / (2 * 8**2))  # Gaussian around 35‰

ax7.plot(temp_range, intensity_temp, 'r-', linewidth=3, label='Temperature Effect')
ax7_twin = ax7.twinx()
ax7_twin.plot(salinity_range, intensity_sal, 'b-', linewidth=3, label='Salinity Effect')

ax7.set_xlabel('Temperature (°C)')
ax7.set_ylabel('Intensity (%) - Temperature', color='red')
ax7_twin.set_ylabel('Intensity (%) - Salinity', color='blue')
ax7.set_title('Environmental Effects on Bioluminescence', fontweight='bold', fontsize=14)
ax7.grid(True, alpha=0.3)

# Color the y-axis labels
ax7.tick_params(axis='y', labelcolor='red')
ax7_twin.tick_params(axis='y', labelcolor='blue')

# Add optimal zones
ax7.axvspan(20, 30, alpha=0.2, color='red', label='Optimal Temp Range')
ax7_twin.axvspan(30, 40, alpha=0.2, color='blue', label='Optimal Salinity Range')
save_and_close("07_environmental_sensitivity")

# 8. Protocol Stack
fig, ax8 = plt.subplots(figsize=(10, 8))
ax8.set_xlim(0, 10)
ax8.set_ylim(0, 10)
ax8.set_title('Bio-Native Protocol Stack', fontweight='bold', fontsize=14)

stack_layers = [
    ('Application Layer', 8.5, 'lightblue', 'Bio-App Interface'),
    ('Transport Layer', 7, 'lightgreen', 'Reliability & Flow Control'),
    ('Network Layer', 5.5, 'lightyellow', 'Bio-Routing Protocols'),
    ('Data Link Layer', 4, 'lightcoral', 'Bio-Frame Structure'),
    ('Physical Layer', 2.5, 'lightgray', 'Bioluminescent Signaling'),
    ('Bio Layer', 1, 'gold', 'Organism Control')
]

for layer, y_pos, color, description in stack_layers:
    layer_rect = FancyBboxPatch((1, y_pos-0.4), 8, 0.8, boxstyle="round,pad=0.05", 
                               facecolor=color, edgecolor='black', linewidth=2)
    ax8.add_patch(layer_rect)
    ax8.text(2, y_pos, layer, va='center', fontweight='bold')
    ax8.text(7.5, y_pos, description, va='center', style='italic', fontsize=9)

# Add data flow arrows
for i in range(len(stack_layers)-1):
    y_start = stack_layers[i][1] - 0.4
    y_end = stack_layers[i+1][1] + 0.4
    arrow = FancyArrowPatch((0.5, y_start), (0.5, y_end), arrowstyle='<->', 
                           mutation_scale=15, color='purple', linewidth=2)
    ax8.add_patch(arrow)

ax8.text(0.2, 5, 'Data\nFlow', ha='center', va='center', rotation=90, 
         fontweight='bold', color='purple')

ax8.set_xticks([])
ax8.set_yticks([])
ax8.axis('off')
save_and_close("08_protocol_stack")

# 9. Synthetic Gene Circuit
fig, ax9 = plt.subplots(figsize=(15, 8))
ax9.set_xlim(0, 15)
ax9.set_ylim(0, 8)
ax9.set_title('Synthetic Gene Circuit for Bio-LiFi Control', fontweight='bold', fontsize=14)

# Input signal
input_box = FancyBboxPatch((0.5, 6), 2, 1, boxstyle="round,pad=0.1", 
                          facecolor='lightblue', edgecolor='blue', linewidth=2)
ax9.add_patch(input_box)
ax9.text(1.5, 6.5, 'Input Signal', ha='center', va='center', fontweight='bold')

# Promoter
promoter_box = FancyBboxPatch((3.5, 6), 2, 1, boxstyle="round,pad=0.1", 
                             facecolor='lightgreen', edgecolor='green', linewidth=2)
ax9.add_patch(promoter_box)
ax9.text(4.5, 6.5, 'Promoter', ha='center', va='center', fontweight='bold')

# Gene expression
gene_box = FancyBboxPatch((6.5, 6), 2, 1, boxstyle="round,pad=0.1", 
                         facecolor='lightyellow', edgecolor='orange', linewidth=2)
ax9.add_patch(gene_box)
ax9.text(7.5, 6.5, 'Luciferase\nGene', ha='center', va='center', fontweight='bold')

# Protein production
protein_box = FancyBboxPatch((9.5, 6), 2, 1, boxstyle="round,pad=0.1", 
                            facecolor='lightcoral', edgecolor='red', linewidth=2)
ax9.add_patch(protein_box)
ax9.text(10.5, 6.5, 'Luciferase\nProtein', ha='center', va='center', fontweight='bold')

# Bioluminescence
bio_output_box = FancyBboxPatch((12.5, 6), 2, 1, boxstyle="round,pad=0.1", 
                               facecolor='gold', edgecolor='darkorange', linewidth=2)
ax9.add_patch(bio_output_box)
ax9.text(13.5, 6.5, 'Light\nOutput', ha='center', va='center', fontweight='bold')

# Feedback loop
feedback_box = FancyBboxPatch((6, 3), 4, 1, boxstyle="round,pad=0.1", 
                             facecolor='lightgray', edgecolor='gray', linewidth=2)
ax9.add_patch(feedback_box)
ax9.text(8, 3.5, 'Quorum Sensing Feedback', ha='center', va='center', fontweight='bold')

# Add arrows for main pathway
main_arrows = [
    FancyArrowPatch((2.5, 6.5), (3.5, 6.5), arrowstyle='->', mutation_scale=20),
    FancyArrowPatch((5.5, 6.5), (6.5, 6.5), arrowstyle='->', mutation_scale=20),
    FancyArrowPatch((8.5, 6.5), (9.5, 6.5), arrowstyle='->', mutation_scale=20),
    FancyArrowPatch((11.5, 6.5), (12.5, 6.5), arrowstyle='->', mutation_scale=20)
]

for arrow in main_arrows:
    ax9.add_patch(arrow)

# Feedback arrows
feedback_arrows = [
    FancyArrowPatch((10, 6), (9, 4), arrowstyle='->', mutation_scale=15, 
                   color='gray', linestyle='dashed'),
    FancyArrowPatch((7, 4), (4, 5.8), arrowstyle='->', mutation_scale=15, 
                   color='gray', linestyle='dashed')
]

for arrow in feedback_arrows:
    ax9.add_patch(arrow)

# Add substrate
substrate_box = FancyBboxPatch((9.5, 3.8), 2, 0.8, boxstyle="round,pad=0.05", 
                              facecolor='lightcyan', edgecolor='cyan', linewidth=1)
ax9.add_patch(substrate_box)
ax9.text(10.5, 4.2, 'Luciferin\n(Substrate)', ha='center', va='center', fontsize=9)

substrate_arrow = FancyArrowPatch((10.5, 4.6), (10.5, 6), arrowstyle='->', 
                                 mutation_scale=15, color='cyan')
ax9.add_patch(substrate_arrow)

ax9.set_xticks([])
ax9.set_yticks([])
ax9.axis('off')
save_and_close("09_synthetic_gene_circuit")

print("\nBio-LiFi Communication Systems Visualization Complete!")
print(f"\nAll PNG files saved to: {output_dir}/")
print("\nGenerated files:")
print("1. 01_bioluminescent_control_mechanisms.png")
print("2. 02_multi_wavelength_channels.png")
print("3. 03_photoreceptor_network_structure.png")
print("4. 04_system_architecture.png")
print("5. 05_signal_transduction_timeline.png")
print("6. 06_event_driven_communication.png")
print("7. 07_environmental_sensitivity.png")
print("8. 08_protocol_stack.png")
print("9. 09_synthetic_gene_circuit.png")