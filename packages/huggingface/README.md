HuggingFace Hub (huggingface_hub) v1.27.0

CLI (huggingface-cli):
  huggingface-cli login                      authenticate with an HF token
  huggingface-cli whoami                     show current user
  huggingface-cli download <model> ...       download a model/dataset
  huggingface-cli upload <model> ...         publish files

Python:
  from huggingface_hub import snapshot_download
  snapshot_download("org/model")

Docs: https://huggingface.co/docs/huggingface_hub

Note: Termux uses classic HTTP downloads (HF_HUB_DISABLE_XET=1, set via
etc/profile.d/huggingface.sh) because the optional hf-xet accelerator has no
Termux wheel and is incompatible with Python 3.14. Remove the variable if a
working hf-xet ships in the future.