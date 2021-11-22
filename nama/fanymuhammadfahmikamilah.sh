#!/bin/bash

tampilNama () {
    printf '%s ' "$1"
}

namaPerkata=( "Fany" "Muhammad" "Fahmi" "Kamilah")

for kata in "${namaPerkata[@]}"; do
    tampilNama "$kata"
done