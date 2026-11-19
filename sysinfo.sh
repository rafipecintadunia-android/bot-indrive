#!/data/data/com.termux/files/usr/bin/bash

# Kode Warna ANSI
C1='\e[1;36m' # Cyan Terang (Logo & Label)
C2='\e[1;32m' # Hijau Terang (Header)
C3='\e[1;33m' # Kuning (Garis)
NC='\e[0m'    # Reset Warna

# Pengambilan Data Baterai (via Termux-API)
if command -v termux-battery-status >/dev/null 2>&1; then
    BAT_JSON=$(termux-battery-status 2>/dev/null)
    BAT_PCT=$(echo "$BAT_JSON" | jq -r '.percentage // "N/A"')
    BAT_TEMP=$(echo "$BAT_JSON" | jq -r '.temperature // "N/A"')
    BAT_STAT=$(echo "$BAT_JSON" | jq -r '.status // "N/A"')
    BAT_INFO="${BAT_PCT}% (${BAT_STAT}) - ${BAT_TEMP}°C"
else
    BAT_INFO="Paket termux-api belum aktif"
fi

# Pengambilan Data Jaringan
IP_LOKAL=$(ifconfig 2>/dev/null | awk '/inet / && $2 != "127.0.0.1" {print $2; exit}')
[ -z "$IP_LOKAL" ] && IP_LOKAL="Tidak terhubung"
IP_PUBLIK=$(curl -s --max-time 3 ifconfig.me || echo "Offline / Timeout")

# Data Sistem
MODEL="$(getprop ro.product.brand) $(getprop ro.product.model)"
ANDROID="Android $(getprop ro.build.version.release)"
RAM=$(free -h | awk '/^Mem:/ {print $3 " / " $2}')
DISK=$(df -h /data | awk 'NR==2 {print $3 " / " $2 " (" $5 ")"}')
UPTIME=$(uptime -p 2>/dev/null | sed 's/up //' || uptime | awk -F'( |,|:)+' '{print $6" jam "$7" mnt"}')

# Tampilan Output Gaya Neofetch
clear
echo -e "${C1}       .---.        ${C2}root@CPH2895${NC}"
echo -e "${C1}      /     \\       ${C3}----------------------------------------${NC}"
echo -e "${C1}     | () () |      ${C1}Device    :${NC} $MODEL"
echo -e "${C1}      \\  ^  /       ${C1}OS        :${NC} $ANDROID"
echo -e "${C1}       |||||        ${C1}Firmware  :${NC} CPH2895export_16_A.69"
echo -e "${C1}       |||||        ${C1}Kernel    :${NC} 5.15.189-android13-8-00013"
echo -e "${C1}      /     \\       ${C1}Build     :${NC} Sun, 09 Nov 2025 20:47:23 WIB"
echo -e "${C1}     '-------'      ${C1}Uptime    :${NC} $UPTIME"
echo -e "                    ${C1}RAM       :${NC} $RAM"
echo -e "                    ${C1}Storage   :${NC} $DISK"
echo -e "                    ${C1}Baterai   :${NC} $BAT_INFO"
echo -e "                    ${C1}IP Lokal  :${NC} $IP_LOKAL"
echo -e "                    ${C1}IP Publik :${NC} $IP_PUBLIK"
echo -e "                    ${C3}----------------------------------------${NC}"
echo -e "                    \e[41m   \e[42m   \e[43m   \e[44m   \e[45m   \e[46m   \e[0m"
echo ""
