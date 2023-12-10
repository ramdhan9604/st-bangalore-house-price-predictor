mkdir -p ~/.streamlit/

cat <<EOL > ~/.streamlit/config.toml
[server]
port = $PORT
enableCORS = false
headless = true

[theme]
base = 'Custom Theme'
primaryColor = '#F11212'
backgroundColor = '#E8DAE8'
secondaryBackgroundColor = '#E3E5E6'
textColor = '#030A20'
font = 'Serif'
EOL
