# Blender Universal File Importer 🗃️

**A Blender add-on for safe importing of 3D assets (FBX/OBJ/GLTF/BLEND) with isolated context and preview capabilities**

![Add-on Demo](https://archive.org/download/rotatingfood2/06d99c_ec144b0a749e4cc0b43cdaf414a12766_mv2.gif) <!-- Replace with actual demo GIF -->

## Features ✨
- **Isolated Import Context** - Prevents scene contamination
- **Multi-format Support** - FBX, OBJ, GLB/GLTF, BLEND files
- **Auto Cleanup** - Removes temporary data after import
- **Error Handling** - Detailed reporting for import issues
- **File Browser Integration** - Direct access from Blender's import panel

## Download & Installation 📥

### Option 1: Blender Market (Recommended)
[![Blender Market](https://img.shields.io/badge/Blender_Market-Download-FF9900)](https://www.blendermarket.com/products/your-addon)  
Official store version with automatic updates

### Option 2: GitHub Releases
[![GitHub Release](https://img.shields.io/badge/GitHub-Download-181717)](https://github.com/yourusername/blender_universal_file_importer/releases)  
Latest development version (manual updates)

### Installation Steps
![Installation Guide](https://via.placeholder.com/600x300.png?text=Installation+Steps+Screenshot)
1. Download the `.zip` file from your preferred source
2. Open Blender → `Edit > Preferences > Add-ons`
3. Click `Install...` and select the downloaded file
4. Enable the checkbox next to "Universal File Importer"

## Usage 🛠️

### Basic Import Workflow
1. Open Blender's File Browser (`File > Import`)
   ![Open Browser](https://github.com/rafaeldtr41/blender_universal_file_importer/blob/main/images/Captura%20de%20pantalla%202025-03-21%20222323.png)
3. Navigate to your model file
4. **Activate the Import Panel**  
   - Press `N` to open sidebar
   - Select "Import" category

5. Click **"Clean Import"** button  
   
6. View imported model in isolated context  
   ![Imported Model]([https://via.placeholder.com/800x400.png?text=Imported+Model+Preview](https://github.com/rafaeldtr41/blender_universal_file_importer/blob/main/images/Captura%20de%20pantalla%202025-03-21%20222806.png))

## Supported Formats 📄

| Format | Features | Notes |
|--------|----------|-------|
| `.fbx` | Full scene import | Automatic material setup |
| `.obj` | Mesh preservation | UVs & normals support |
| `.glb` | PBR materials | Animation support |
| `.blend` | Object linking | Collection support |

## Support the Project ☕

If you find this add-on useful, consider supporting its development:

### Buy Me a Coffee
![Buy Me A Coffee](https://github.com/rafaeldtr41/blender_universal_file_importer/blob/main/images/Screenshot_2025-03-21-18-36-47-635_com.wallet.crypto.trustapps.jpg))]  
**USDT (TRC20):**  
```
0x5d85bA08C433219B06a94BeCc68C4ccbc6c97857
```

[Click here to donate via USDT](https://your-donation-link.com)

Your support helps maintain and improve this project!

## Troubleshooting ⚠️

**Q: Missing import button?**  
```bash
# Enable required Blender importers:
Edit > Preferences > Add-ons
- Search "IO" > Enable all official importers
```

**Q: Objects not appearing?**  
```python
# Check:
1. File format support
2. Console for error messages
3. Scene collection hierarchy
```

## Contributing 🤝

We welcome contributions! Please follow our [contribution guidelines](CONTRIBUTING.md).

## License 📄

MIT License - See [LICENSE](LICENSE) for details

---

**Tested with:**  
![Blender Version](https://img.shields.io/badge/Blender-4.3.0+-orange)
