# HeritageLens

**AI-powered cultural heritage preservation through computer vision and 3D reconstruction.**

HeritageLens is an open-source nonprofit platform that digitally preserves monuments, archaeological sites, and cultural landmarks using computer vision. Anyone, anywhere in the world can upload photos of a heritage site — we turn them into searchable, analysable digital records and 3D reconstructions, creating a permanent archive of human history before it disappears.

---

## Why This Exists

Every year, cultural heritage sites are lost to war, climate change, urban development, and neglect. Once a monument is gone, it is gone forever — along with the history, identity, and memory it carried.

HeritageLens exists to make sure that never has to be the final word.

We believe that the tools to preserve human history should be free, open, and available to everyone — not locked behind institutional budgets or government access. A student in Melbourne, a photographer in Nairobi, a local historian in Baghdad should all be able to contribute to the permanent record of our shared world.

---

## What It Does

- **Upload** — submit photos of any cultural heritage site from anywhere in the world
- **Process** — computer vision pipeline analyses, annotates, and processes each submission
- **Reconstruct** — multi-image submissions are used to generate 3D reconstructions of sites
- **Archive** — every record is stored with structured metadata and made permanently searchable
- **Share** — the dataset is open for researchers, educators, and heritage organisations to use

---

## Current Status

🟡 **Active development — v0.1**

The core image processing pipeline is being built. Contributions and feedback welcome.

---

## Tech Stack

- **Python** — core pipeline
- **OpenCV** — image processing and analysis
- **PyTorch** — deep learning components (in development)
- **Neural Radiance Fields (NeRF)** — 3D reconstruction (in development)
- **Azure** — cloud storage and compute

---

## Getting Started

### Prerequisites

```bash
python 3.9+
pip
git
```

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/heritagelens.git
cd heritagelens
pip install -r requirements.txt
```

### Run the basic pipeline

```bash
python pipeline.py --image path/to/your/image.jpg
```

This will process your image and save the output alongside a JSON metadata record.

---

## Project Structure

```
heritagelens/
├── pipeline.py          # Core image processing pipeline
├── monument.py          # Monument data model
├── requirements.txt     # Dependencies
├── data/                # Sample data and schemas
├── outputs/             # Processed outputs
└── docs/                # Documentation
```

---

## Roadmap

- [x] Project foundation and data schema
- [x] Basic image processing pipeline (OpenCV)
- [ ] Web upload interface
- [ ] Multi-image 3D reconstruction
- [ ] NeRF-based dense reconstruction
- [ ] Public dataset release
- [ ] UNESCO partnership integration
- [ ] Global community campaigns

---

## Contributing

HeritageLens is open source and community-driven. Whether you're a developer, researcher, photographer, or just someone who cares about cultural heritage — there is a place for you here.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more detail.

---

## Research

HeritageLens is built in parallel with active research into scalable Neural Radiance Fields for cultural heritage digitisation, conducted in collaboration with the University of Melbourne AI Lab. Research updates and preprints will be linked here as they become available.

---

## License

MIT License — see [LICENSE](LICENSE) for details.

Free to use, modify, and build on. We only ask that you share what you build.

---

## Contact

Built by **Mustafa Ali** — Melbourne, Australia.

If you represent a heritage organisation, research institution, or media outlet and want to get in touch:

📧 mustafa74589@gmail.com
🌐 [your website here]
🐦 Twitter(X) = @NeRFpro999

---

*Preserving the past. One upload at a time.*
