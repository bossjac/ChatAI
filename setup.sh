mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
base = 'light'\n\
\n\
" > ~/.streamlit/config.toml
pip install -r requirements.txt
