Creating SSH key:
ssh-keygen -t ed25519 -c "alpatov.av@phystech.edu"
SSH agent setting:
eval "$(ssh-agent -s)"
ssh add ~/.ssh/id_ed25519
