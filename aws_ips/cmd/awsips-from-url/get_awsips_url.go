package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
)

// Prefixes struct contains an array of ip prefixes
type Prefixes struct {
	Prefixes []Prefix `json:"prefixes"`
}

// Prefix struct contains IP Prefix, Region, Service and Network Border Group
type Prefix struct {
	IP_Prefix            string `json:"ip_prefix"`
	Region               string `json:"region"`
	Service              string `json:"service"`
	Network_Border_Group string `json:"network_border_group"`
}

func main() {

	url := "https://ip-ranges.amazonaws.com/ip-ranges.json"
	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	var prefixes Prefixes
	err = json.NewDecoder(resp.Body).Decode(&prefixes)
	if err != nil {
		log.Fatal(err)
	}

	// Appends a line of text to a file or creates the file if it doesn't exist.
	f, err := os.OpenFile("US_REGION_AWS_IPS-2", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0644)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	for i := 0; i < len(prefixes.Prefixes); i++ {

		if prefixes.Prefixes[i].Region == "us-east-1" {
			f.WriteString(prefixes.Prefixes[i].IP_Prefix + "\n")
		}
		if prefixes.Prefixes[i].Region == "us-east-2" {
			f.WriteString(prefixes.Prefixes[i].IP_Prefix + "\n")
		}
		if prefixes.Prefixes[i].Region == "us-west-1" {
			f.WriteString(prefixes.Prefixes[i].IP_Prefix + "\n")
		}
		if prefixes.Prefixes[i].Region == "us-west-2" {
			f.WriteString(prefixes.Prefixes[i].IP_Prefix + "\n")
		}

	}
}
