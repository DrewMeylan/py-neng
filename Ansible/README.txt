Inventory File
  IP, Hostnames or FQDN (Latter two require name resolution)
  Managed IP addresses should be static or DHCP reserved

SSH Setup
  MAKE OWN SSH KEY

  MAKE ANSIBLE SSH KEY
  ssh-keygen -t ed25519 -C "Ansible key"
  ssh-copy-id -i {SSH_Key_file} {Remote Host IP} # You must be able to SSH into the remote host w own key

  
