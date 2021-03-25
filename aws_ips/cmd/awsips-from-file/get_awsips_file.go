package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
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
	// Open json file
	jsonFile, err := os.Open("example.json")
	if err != nil {
		fmt.Println(err)
	}

	defer jsonFile.Close()

	// Read the opened jsonFile as a byte array
	byteValue, _ := ioutil.ReadAll(jsonFile)

	// Defining a prefixes array
	var prefixes Prefixes

	// Unmarshall the byteArray which contains contents from the JSON file to prefixes
	json.Unmarshal(byteValue, &prefixes)

	// Appends a line of text to a file or creates the file if it doesn't exist.
	f, err := os.OpenFile("US_REGION_AWS_IPS", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	// This loops through the file, find section of the file that contains the specified region
	// reads the ip information and writes it to a file.
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
