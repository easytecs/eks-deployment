for i in $(${{ inputs.secrets }}); do echo "  $i: ${!i}" >> ./secrets.yaml ; done