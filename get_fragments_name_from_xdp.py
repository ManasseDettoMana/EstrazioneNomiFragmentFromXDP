import os
import xml.etree.ElementTree as ET
import re
import tkinter as tk
from tkinter import filedialog

def main():
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(title="Seleziona un file .xdp", filetypes=[("XDP files", "*.xdp")])
    
    if not file_path:
        print("Nessun file selezionato.")
        return
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Trova tutti i riferimenti con la gerarchia mantenuta
        matches = list(re.finditer(r"\.\\Fragment\\(M047[^\\]*?\.xdp)", content))
        
        fragments = []
        seen = set()
        
        for match in matches:
            fragment = match.group(1)
            if fragment not in seen:
                fragments.append(fragment)
                seen.add(fragment)
        
        if fragments:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            output_file_name = f"{os.path.basename(file_path).split('.xdp')[0]}_tags.txt"
            output_file_path = os.path.join(desktop, output_file_name)
            
            with open(output_file_path, "w", encoding="utf-8") as f:
                for fragment in fragments:  # Mantiene l'ordine originale
                    f.write(fragment + "\n")
            
            print(f"I tag sono stati salvati in {output_file_path}")
        else:
            print("Nessun tag trovato nel file.")
    
    except Exception as e:
        print(f"Errore nell'analisi del file: {e}")

if __name__ == "__main__":
    main()
