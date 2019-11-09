python3 -m venv /opt/RecordEnv
source /opt/RecordEnv/bin/activate
echo "Virtual environment (RecordEnv) has been created"
echo ""
echo "Installing the Python dependencies"
/opt/RecordEnv/bin/pip3 install --upgrade pip
chmod +x record_reqs.sh
./record_reqs.sh
echo ""
echo "All Python dependencies has been installed"
