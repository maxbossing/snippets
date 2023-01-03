#!/usr/bin/env bash
#
# This Script generates pgp keys

echo "Please enter your Real Name."
read -p "Name: " name
echo "Please enter your Real Email."
read -p "Email: " email

# generates the master cert key
gpg --quick-gen-key "$name <$email>" rsa4096 cert 0

# generates auth, enc and sign keys with cert key
gpg --quick-add-key $(gpg --fingerprint $email | sed -n '/^\s/s/\s*//p' | sed -e 's/\ //g') rsa4096 sign 3y
gpg --quick-add-key $(gpg --fingerprint $email | sed -n '/^\s/s/\s*//p' | sed -e 's/\ //g') rsa4096 encrypt 3y
gpg --quick-add-key $(gpg --fingerprint $email | sed -n '/^\s/s/\s*//p' | sed -e 's/\ //g') rsa4096 auth 3y