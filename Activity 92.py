from flask import Flask, render_template_string, jsonify, request

app = Flask(__name__)

# Simulated in-memory database for smart devices
devices = [
    {"id": 1, "name": "Living Room Light", "type": "Lighting", "status": "On", "value": "80%"},
    {"id": 2, "name": "Main AC Thermostat", "type": "Climate", "status": "On", "value": "72°F"},
    {"id": 3, "name": "Front Door Lock", "type": "Security", "status": "Locked", "value": "N/A"},
    {"id": 4, "name": "Garage Door", "type": "Security", "status": "Closed", "value": "N/A"},
    {"id": 5, "name": "Kitchen Speaker", "type": "Audio", "status": "Off", "value": "0%"}
]

# Frontend Dashboard Template (HTML + Tailwind CSS + JavaScript Fetch API)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Device Command Center</title>
    <!-- Tailwind CSS for modern styling -->
    <script src="https://tailwindcss.com"></script>
</head>
<body class="bg-gray-950 text-gray-100 font-sans min-h-screen">

    <div class="container mx-auto p-4 md:p-8 max-w-7xl">
        <!-- Header -->
        <header class="mb-8 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 border-b border-gray-800 pb-6">
            <div>
                <h1 class="text-3xl font-extrabold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-teal-400">
                    Smart Command Hub
                </h1>
                <p class="text-sm text-gray-400 mt-1">Centralized device telemetry and remote execution system.</p>
            </div>
            <div class="flex items-center gap-2 bg-gray-900 border border-gray-800 px-4 py-2 rounded-lg">
                <span class="relative flex h-3 w-3">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
                </span>
                <span class="text-xs font-mono font-semibold tracking-wider text-green-400 uppercase">System Operational</span>
            </div>
        </header>

        <!-- Analytics Overview Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
            <div class="bg-gray-900 border border-gray-800 p-5 rounded-xl">
                <p class="text-xs font-semibold uppercase tracking-wider text-gray-400">Total Managed Devices</p>
                <p class="text-2xl font-bold mt-1 text-white" id="total-count">{{ devices|length }}</p>
            </div>
            <div class="bg-gray-900 border border-gray-800 p-5 rounded-xl">
                <p class="text-xs font-semibold uppercase tracking-wider text-gray-400">Active Power Consumption</p>
                <p class="text-2xl font-bold mt-1 text-teal-400">1.42 kW</p>
            </div>
            <div class="bg-gray-900 border border-gray-800 p-5 rounded-xl sm:col-span-2 lg:col-span-1">
                <p class="text-xs font-semibold uppercase tracking-wider text-gray-400">Network Status</p>
                <p class="text-2xl font-bold mt-1 text-blue-400">98.7% Signal</p>
            </div>
        </div>

        <!-- Main Device Control Grid -->
        <h2 class="text-xl font-bold text-gray-200 mb-4 flex items-center gap-2">
            <span>Peripherals Matrix</span>
        </h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {% for device in devices %}
            <div class="bg-gray-900 border border-gray-800 rounded-xl p-6 shadow-xl transition-all duration-200 hover:border-gray-700 flex flex-col justify-between">
                <div>
                    <!-- Card Top Row -->
                    <div class="flex justify-between items-start gap-2 mb-3">
                        <div>
                            <span class="text-[10px] font-bold uppercase tracking-widest text-blue-400 bg-blue-950/50 border border-blue-900 px-2 py-0.5 rounded">
                                {{ device.type }}
                            </span>
                            <h3 class="text-lg font-bold text-white mt-2 tracking-tight">{{ device.name }}</h3>
                        </div>
                        
                        <!-- Status Badge Component -->
                        <span id="badge-{{ device.id }}" class="px-2.5 py-1 rounded-md text-xs font-bold transition-colors duration-200
                            {% if device.status in ['On', 'Locked', 'Closed'] %}
                                bg-emerald-950 text-emerald-400 border border-emerald-800
                            {% else %}
                                bg-gray-800 text-gray-400 border border-gray-700
                            {% endif %}">
                            {{ device.status }}
                        </span>
                    </div>

                    <!-- Diagnostics Metadata Area -->
                    <div class="my-4 py-3 border-y border-gray-800/60 flex justify-between items-center text-sm">
                        <span class="text-gray-400">Operational Level:</span>
                        <span id="value-{{ device.id }}" class="font-mono font-bold text-gray-200">{{ device.value }}</span>
                    </div>
                </div>

                <!-- Interactive Trigger Buttons -->
                <div class="mt-4 pt-2">
                    <button onclick="dispatchToggle({{ device.id }})" 
                            class="w-full bg-gray-800 hover:bg-gray-700 text-white font-medium text-sm py-2 px-4 rounded-lg transition-colors border border-gray-700 active:scale-[0.98]">
                        Trigger State Action
                    </button>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <!-- Async Frontend State Orchestrator -->
    <script>
        function dispatchToggle(deviceId) {
            // Asynchronous API call to update device state on the backend safely
            fetch(`/api/device/${deviceId}/toggle`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
            })
            .then(response => {
                if (!response.ok) throw new Error('Network failure or invalid node ID');
                return response.json();
            })
            .then(data => {
                // Update specific elements directly to prevent a full page flash/reload
                const badge = document.getElementById(`badge-${deviceId}`);
                const valueText = document.getElementById(`value-${deviceId}`);
                
                badge.innerText = data.status;
                valueText.innerText = data.value;

                // Adjust layout styles based on fresh real-time states
                if (['On', 'Locked', 'Closed'].includes(data.status)) {
                    badge.className = "px-2.5 py-1 rounded-md text-xs font-bold transition-colors duration-200 bg-emerald-950 text-emerald-400 border border-emerald-800";
                } else {
                    badge.className = "px-2.5 py-1 rounded-md text-xs font-bold transition-colors duration-200 bg-gray-800 text-gray-400 border border-gray-700";
                }
            })
            .catch(error => console.error('Command Execution Interrupted:', error));
        }
    </script>
</body>
</html>
'''

# --- BACKEND ROUTING ---

@app.route('/')
def index():
    """Renders the main dashboard webpage containing active device cards."""
    return render_template_string(HTML_TEMPLATE, devices=devices)

@app.route('/api/device/<int:device_id>/toggle', methods=['POST'])
def handle_device_toggle(device_id):
    """
    API endpoint executing device status toggles.
    Swaps states and changes mock data logic depending on device type.
    """
    for device in devices:
        if device['id'] == device_id:
            # Match current status and toggle state pairs
            if device['status'] == 'On':
                device['status'] = 'Off'
                if "%" in device['value']: device['value'] = '0%'
            elif device['status'] == 'Off':
                device['status'] = 'On'
                if "%" in device['value']: device['value'] = '80%'
            elif device['status'] == 'Locked':
                device['status'] = 'Unlocked'
            elif device['status'] == 'Unlocked':
                device['status'] = 'Locked'
            elif device['status'] == 'Closed':
                device['status'] = 'Open'
            elif device['status'] == 'Open':
                device['status'] = 'Closed'

            return jsonify(device), 200

    return jsonify({"error": "Device entity requested was not found"}), 404

if __name__ == '__main__':
    # Run the micro web framework on local machine port 5000
    app.run(debug=True, port=5000)