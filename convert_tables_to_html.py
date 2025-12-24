#!/usr/bin/env python3
"""
Convert markdown tables to HTML tables with truncated addresses and copy functionality
"""
import re

def truncate_address(address):
    """Truncate address to first 6 and last 4 characters"""
    if not address or len(address) < 10:
        return address
    return f"{address[:6]}...{address[-4:]}"

def parse_table_row(line):
    """Parse a markdown table row into columns"""
    # Remove leading/trailing pipes and split by |
    parts = [p.strip() for p in line.strip().split('|') if p.strip()]
    if len(parts) >= 5:
        return {
            'address': parts[0],
            'contract_name': parts[1],
            'wat': parts[2],
            'risk_level': parts[3],
            'risk_description': parts[4]
        }
    return None

def generate_address_cell(address):
    """Generate HTML cell with truncated address and copy functionality"""
    truncated = truncate_address(address)
    return f'''<td style={{ fontFamily: 'monospace', fontSize: '0.9rem', width: '12%' }}>
  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
    <span 
      onClick={() => {{
        navigator.clipboard.writeText('{address}');
        const btn = event.target.closest('div').querySelector('.copy-btn');
        if (btn) {{
          btn.textContent = 'Copied!';
          setTimeout(() => {{ btn.textContent = '📋'; }}, 2000);
        }}
      }}}
      style={{ cursor: 'pointer', color: '#4063FF' }}
      title="Click to copy full address"
    >
      {truncated}
    </span>
    <button
      className="copy-btn"
      onClick={(e) => {{
        e.stopPropagation();
        navigator.clipboard.writeText('{address}');
        e.target.textContent = 'Copied!';
        setTimeout(() => {{ e.target.textContent = '📋'; }}, 2000);
      }}}
      style={{
        background: 'none',
        border: 'none',
        cursor: 'pointer',
        fontSize: '0.9rem',
        padding: '0.25rem',
        color: '#666'
      }}
      title="Copy address"
    >
      📋
    </button>
  </div>
</td>'''

def convert_table_section(lines, start_idx, end_idx):
    """Convert a markdown table section to HTML"""
    rows = []
    for i in range(start_idx, end_idx):
        line = lines[i].strip()
        if line.startswith('|') and not line.startswith('|  -----------'):
            row_data = parse_table_row(line)
            if row_data:
                rows.append(row_data)
    
    if not rows:
        return None
    
    # Generate HTML table
    html = ['<div style={{ overflowX: "auto", marginBottom: "2rem" }}>']
    html.append('<table style={{ width: "100%", borderCollapse: "collapse", fontSize: "0.9rem" }}>')
    html.append('<thead>')
    html.append('<tr style={{ backgroundColor: "#f5f5f5", borderBottom: "2px solid #ddd" }}>')
    html.append('<th style={{ padding: "0.75rem", textAlign: "left", width: "12%" }}>Address</th>')
    html.append('<th style={{ padding: "0.75rem", textAlign: "left", width: "15%" }}>Contract Name</th>')
    html.append('<th style={{ padding: "0.75rem", textAlign: "left", width: "8%" }}>WAT</th>')
    html.append('<th style={{ padding: "0.75rem", textAlign: "left", width: "10%" }}>Risk Level</th>')
    html.append('<th style={{ padding: "0.75rem", textAlign: "left", width: "55%" }}>Risk Description</th>')
    html.append('</tr>')
    html.append('</thead>')
    html.append('<tbody>')
    
    for row in rows:
        html.append('<tr style={{ borderBottom: "1px solid #eee" }}>')
        html.append(generate_address_cell(row['address']))
        html.append(f'<td style={{ padding: "0.75rem", width: "15%" }}>{row["contract_name"]}</td>')
        html.append(f'<td style={{ padding: "0.75rem", width: "8%" }}>{row["wat"]}</td>')
        html.append(f'<td style={{ padding: "0.75rem", width: "10%" }}>{row["risk_level"]}</td>')
        html.append(f'<td style={{ padding: "0.75rem", width: "55%", lineHeight: "1.5" }}>{row["risk_description"]}</td>')
        html.append('</tr>')
    
    html.append('</tbody>')
    html.append('</table>')
    html.append('</div>')
    
    return '\n'.join(html)

def process_file(file_path):
    """Process the file and convert tables"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a table header
        if '|  Address  | ContractName |' in line:
            # Find the table section
            start_idx = i
            # Skip header and separator
            i += 2
            # Find end of table (next ### or empty lines)
            end_idx = i
            while end_idx < len(lines):
                check_line = lines[end_idx].strip()
                if check_line.startswith('###'):
                    break
                if not check_line and end_idx + 1 < len(lines):
                    if lines[end_idx + 1].strip().startswith('###'):
                        break
                if check_line and not check_line.startswith('|'):
                    if end_idx > start_idx + 2:  # At least header + separator + one row
                        break
                end_idx += 1
            
            # Convert table
            html_table = convert_table_section(lines, start_idx, end_idx)
            if html_table:
                result_lines.append(html_table)
                i = end_idx
            else:
                result_lines.append(line.rstrip('\n'))
                i += 1
        else:
            result_lines.append(line.rstrip('\n'))
            i += 1
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result_lines) + '\n')
    
    print(f"Converted tables in {file_path}")

if __name__ == '__main__':
    file_path = '/Users/wilsonwu/Desktop/HashDitDocs/blog/2023-08-24/2023-08-24.mdx'
    process_file(file_path)

