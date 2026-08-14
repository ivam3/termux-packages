Cactus - Hybrid edge-cloud AI engine (v2.0.1)

Usage:
  cactus auth <pat|hf>                authenticate against HuggingFace / Cactus
  cactus download <model>             download a model
  cactus list                         list cached models
  cactus run <model>                  run a model (e.g. Cactus-Compute/needle)
  cactus transcribe <model> --file f  speech transcription
  cactus serve <model> --port 8080    OpenAI-compatible API
  cactus convert <HF model>           convert weights (needs convert stack)
  cactus build --python               rebuild the native engine

Install:  ~/.local/share/cactus
Engine:   ~/.local/share/cactus/cactus-engine/build/libcactus_engine.so
Weights:  ~/.local/share/cactus/weights
Log:      ~/.local/share/cactus/build.log

Help: https://t.me/Ivam3_Bot
Issues: https://github.com/cactus-compute/cactus