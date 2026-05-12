cp client.py ./mineru/cli/client.py
cp models_download_utils.py ./mineru/utils/models_download_utils.py
cp Image.py ./.venv/lib/python3.13/site-packages/PIL/Image.py
source .venv/bin/activate
uv run mineru -p ~/Working/BIDDINGS -o ~/Working/BIDDINGS 

