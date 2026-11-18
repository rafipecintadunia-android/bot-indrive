import os
import ipinfo

access_token = os.getenv("IPINFO_TOKEN")
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()

print("[ SUCCESS ] Berhasil terhubung ke Server IPinfo!")
print(f"IP Publik : {details.ip}")
print(f"Kota      : {details.city}, {details.region} ({details.country})")
print(f"Provider  : {details.org}")
