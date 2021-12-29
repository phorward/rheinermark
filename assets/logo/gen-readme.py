#!/usr/bin/python3
import glob, cairosvg, PIL

for svg in reversed(sorted(glob.glob("*.svg"))):
	base = svg.removesuffix(".svg")

	# generate png from svg
	png = base + ".png"
	cairosvg.svg2png(url=svg, write_to=png)
	svg.removesuffix(".svg") + ".png"

	# generate webp from png
	webp = base + ".webp"
	image = PIL.Image.open(png)
	image.save(webp, format="webp")

	print(f"# {base}\n")
	print("\n".join([f"## {x}\n![{x}]({x})\n" for x in [svg, png, webp]]))
