install:
	brew install nodejs npm ffmpeg
	curl -LsSf https://astral.sh/uv/install.sh | sh
	npm install
	uv python install
	uv sync

website:
	npm run dev