"""
Beat Phenomena Simulation - Python Plot Generator
Generates interactive HTML visualization using Python and Plotly
"""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def generate_beat_simulation(A=1, f1=260, f2=252):
    """
    Generate beat phenomena simulation plots
    
    Parameters:
    -----------
    A : float
        Amplitude
    f1 : float
        Frequency 1 in Hz
    f2 : float
        Frequency 2 in Hz
    
    Returns:
    --------
    fig : plotly.graph_objects.Figure
        Plotly figure with subplots
    results : dict
        Calculated results
    """
    
    # Derived parameters
    f_beat = abs(f1 - f2)
    f_avg = (f1 + f2) / 2
    beat_period = 1 / f_beat if f_beat > 0 else float('inf')
    
    # Time array (2 seconds to show multiple beats)
    duration = 2  # seconds
    sampling_rate = 10000  # samples per second
    t = np.linspace(0, duration, int(duration * sampling_rate))
    
    # Individual waves
    wave1 = A * np.sin(2 * np.pi * f1 * t)
    wave2 = A * np.sin(2 * np.pi * f2 * t)
    
    # Resultant wave (superposition)
    resultant = wave1 + wave2
    
    # Envelope (amplitude modulation)
    envelope_upper = 2 * A * np.abs(np.cos(2 * np.pi * f_beat * t / 2))
    envelope_lower = -envelope_upper
    
    # Filter data for zoomed view (first 0.2 seconds)
    zoom_mask = t <= 0.2
    t_zoom = t[zoom_mask]
    wave1_zoom = wave1[zoom_mask]
    wave2_zoom = wave2[zoom_mask]
    resultant_zoom = resultant[zoom_mask]
    envelope_upper_zoom = envelope_upper[zoom_mask]
    envelope_lower_zoom = envelope_lower[zoom_mask]
    
    # Create subplots
    fig = make_subplots(
        rows=4, cols=1,
        subplot_titles=(
            f'<b>Wave 1 (f₁ = {f1} Hz)</b>',
            f'<b>Wave 2 (f₂ = {f2} Hz)</b>',
            '<b>Resultant Wave (Beat Pattern) - Zoomed</b>',
            f'<b>Complete Beat Pattern (Beat Frequency = {f_beat:.1f} Hz)</b>'
        ),
        vertical_spacing=0.08
    )
    
    # Plot 1: First wave (zoomed)
    fig.add_trace(
        go.Scatter(
            x=t_zoom, y=wave1_zoom,
            mode='lines',
            name=f'Wave 1: f₁ = {f1} Hz',
            line=dict(color='#2563eb', width=2)
        ),
        row=1, col=1
    )
    
    # Plot 2: Second wave (zoomed)
    fig.add_trace(
        go.Scatter(
            x=t_zoom, y=wave2_zoom,
            mode='lines',
            name=f'Wave 2: f₂ = {f2} Hz',
            line=dict(color='#dc2626', width=2)
        ),
        row=2, col=1
    )
    
    # Plot 3: Resultant wave with envelope (zoomed)
    fig.add_trace(
        go.Scatter(
            x=t_zoom, y=resultant_zoom,
            mode='lines',
            name='Resultant Wave',
            line=dict(color='#059669', width=2)
        ),
        row=3, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=t_zoom, y=envelope_upper_zoom,
            mode='lines',
            name='Envelope',
            line=dict(color='#0891b2', width=2, dash='dash')
        ),
        row=3, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=t_zoom, y=envelope_lower_zoom,
            mode='lines',
            showlegend=False,
            line=dict(color='#0891b2', width=2, dash='dash')
        ),
        row=3, col=1
    )
    
    # Plot 4: Full duration showing multiple beats
    fig.add_trace(
        go.Scatter(
            x=t, y=resultant,
            mode='lines',
            name='Resultant Wave (Full)',
            line=dict(color='#059669', width=1.5)
        ),
        row=4, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=t, y=envelope_upper,
            mode='lines',
            name='Envelope (Full)',
            line=dict(color='#0891b2', width=2, dash='dash')
        ),
        row=4, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=t, y=envelope_lower,
            mode='lines',
            showlegend=False,
            line=dict(color='#0891b2', width=2, dash='dash')
        ),
        row=4, col=1
    )
    
    # Update axes labels
    fig.update_xaxes(title_text="Time (s)", row=4, col=1)
    fig.update_yaxes(title_text="Amplitude", row=1, col=1)
    fig.update_yaxes(title_text="Amplitude", row=2, col=1)
    fig.update_yaxes(title_text="Amplitude", row=3, col=1)
    fig.update_yaxes(title_text="Amplitude", row=4, col=1)
    
    # Update layout
    fig.update_layout(
        height=1200,
        showlegend=True,
        hovermode='x unified',
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(
            family='Inter, sans-serif',
            size=12,
            color='#0f172a'
        )
    )
    
    # Update grid colors for all subplots
    fig.update_xaxes(gridcolor='#f1f5f9', linecolor='#cbd5e1', zerolinecolor='#94a3b8')
    fig.update_yaxes(gridcolor='#f1f5f9', linecolor='#cbd5e1', zerolinecolor='#94a3b8')
    
    # Results dictionary
    results = {
        'amplitude': A,
        'frequency1': f1,
        'frequency2': f2,
        'beat_frequency': f_beat,
        'average_frequency': f_avg,
        'beat_period': beat_period
    }
    
    return fig, results


def save_to_html(fig, results, filename='beat_simulation_python.html'):
    """
    Save the figure to an HTML file with custom styling
    
    Parameters:
    -----------
    fig : plotly.graph_objects.Figure
        Plotly figure to save
    results : dict
        Calculated results to display
    filename : str
        Output filename
    """
    
    # Create custom HTML with results panel
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beat Phenomena Simulation - Python Generated</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background-color: #f8fafc;
            color: #0f172a;
            padding: 24px;
        }}
        
        .container {{
            max-width: 1600px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            border: 1px solid #e2e8f0;
        }}
        
        .header {{
            background-color: #2563eb;
            color: white;
            padding: 32px 40px;
            border-radius: 8px 8px 0 0;
        }}
        
        .header-content {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 16px;
        }}
        
        .header-title {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        
        .header-icon {{
            width: 48px;
            height: 48px;
            background-color: rgba(255, 255, 255, 0.15);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }}
        
        .header h1 {{
            font-size: 28px;
            font-weight: 700;
        }}
        
        .header-subtitle {{
            font-size: 15px;
            opacity: 0.9;
            margin-top: 4px;
        }}
        
        .badge {{
            background-color: rgba(255, 255, 255, 0.2);
            padding: 6px 12px;
            border-radius: 4px;
            font-size: 13px;
            font-weight: 600;
        }}
        
        .info-panel {{
            margin: 32px 40px;
            padding: 24px;
            background-color: #eff6ff;
            border: 1px solid #bfdbfe;
            border-radius: 6px;
        }}
        
        .info-header {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
        }}
        
        .info-header i {{
            color: #2563eb;
            font-size: 20px;
        }}
        
        .info-header h3 {{
            font-size: 16px;
            font-weight: 600;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
        }}
        
        .info-item {{
            background-color: white;
            padding: 16px;
            border-radius: 6px;
            border: 1px solid #dbeafe;
        }}
        
        .info-item-label {{
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #475569;
            margin-bottom: 6px;
        }}
        
        .info-item-value {{
            font-size: 20px;
            font-weight: 700;
            color: #2563eb;
        }}
        
        .info-item-unit {{
            font-size: 14px;
            font-weight: 500;
            color: #94a3b8;
            margin-left: 4px;
        }}
        
        .plots-section {{
            padding: 32px 40px;
            background-color: #f8fafc;
        }}
        
        .plot-container {{
            background-color: white;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
            overflow: hidden;
        }}
        
        .footer {{
            padding: 24px 40px;
            background-color: #f1f5f9;
            border-top: 1px solid #e2e8f0;
            border-radius: 0 0 8px 8px;
            text-align: center;
        }}
        
        .footer-text {{
            font-size: 14px;
            color: #475569;
            margin-bottom: 12px;
        }}
        
        .footer-formula {{
            font-family: 'Courier New', monospace;
            background-color: white;
            padding: 8px 16px;
            border-radius: 4px;
            border: 1px solid #e2e8f0;
            display: inline-block;
            font-size: 14px;
            font-weight: 600;
            color: #0f172a;
        }}
        
        .footer-meta {{
            font-size: 13px;
            color: #94a3b8;
            margin-top: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-content">
                <div class="header-title">
                    <div class="header-icon">
                        <i class="fas fa-wave-square"></i>
                    </div>
                    <div>
                        <h1>Beat Phenomena Simulation</h1>
                        <div class="header-subtitle">Python Generated Interactive Visualization</div>
                    </div>
                </div>
                <div class="badge">Python + Plotly</div>
            </div>
        </div>
        
        <div class="info-panel">
            <div class="info-header">
                <i class="fas fa-info-circle"></i>
                <h3>Calculated Results</h3>
            </div>
            <div class="info-grid">
                <div class="info-item">
                    <div class="info-item-label">Amplitude</div>
                    <div class="info-item-value">{results['amplitude']:.2f}</div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Frequency 1</div>
                    <div class="info-item-value">
                        {results['frequency1']:.1f}
                        <span class="info-item-unit">Hz</span>
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Frequency 2</div>
                    <div class="info-item-value">
                        {results['frequency2']:.1f}
                        <span class="info-item-unit">Hz</span>
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Beat Frequency</div>
                    <div class="info-item-value">
                        {results['beat_frequency']:.1f}
                        <span class="info-item-unit">Hz</span>
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Average Frequency</div>
                    <div class="info-item-value">
                        {results['average_frequency']:.1f}
                        <span class="info-item-unit">Hz</span>
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-item-label">Beat Period</div>
                    <div class="info-item-value">
                        {results['beat_period']:.3f}
                        <span class="info-item-unit">s</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="plots-section">
            <div class="plot-container" id="plotly-div">
                PLOT_PLACEHOLDER_HERE
            </div>
        </div>
        
        <div class="footer">
            <p class="footer-text">
                Beat phenomena occurs when two waves of slightly different frequencies interfere, creating a periodic variation in amplitude.
            </p>
            <div>
                <span class="footer-formula">f_beat = |f₁ - f₂|</span>
            </div>
            <p class="footer-meta">
                Generated with Python • Plotly.js • NumPy
            </p>
        </div>
    </div>
</body>
</html>
"""
    
    # Generate the plot HTML - use full_html=False to get just the div
    plot_div = fig.to_html(
        include_plotlyjs='cdn',
        full_html=False,
        config={
            'responsive': True,
            'displayModeBar': True,
            'displaylogo': False,
            'scrollZoom': True,
            'doubleClick': 'reset+autosize',
            'toImageButtonOptions': {
                'format': 'png',
                'filename': 'beat_phenomena_simulation',
                'height': 1200,
                'width': 1400,
                'scale': 2
            }
        }
    )
    
    # Combine template with plot
    final_html = html_template.replace('PLOT_PLACEHOLDER_HERE', plot_div)
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print("=" * 60)
    print("BEAT PHENOMENA SIMULATION - PYTHON GENERATED")
    print("=" * 60)
    print(f"Amplitude (A):           {results['amplitude']:.2f}")
    print(f"Frequency 1 (f1):        {results['frequency1']:.1f} Hz")
    print(f"Frequency 2 (f2):        {results['frequency2']:.1f} Hz")
    print(f"Beat Frequency (f_beat): {results['beat_frequency']:.1f} Hz")
    print(f"Average Frequency:       {results['average_frequency']:.1f} Hz")
    print(f"Beat Period:             {results['beat_period']:.3f} s")
    print("=" * 60)
    print(f"\n[SUCCESS] HTML file generated: {filename}")
    print("[INFO] Open this file in your web browser to view the simulation.")
    print("=" * 60)


if __name__ == "__main__":
    # Default parameters
    A = 1
    f1 = 260
    f2 = 252
    
    # Generate simulation
    fig, results = generate_beat_simulation(A, f1, f2)
    
    # Save to HTML
    save_to_html(fig, results, 'beat_simulation_python.html')
