package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
)

func main() {

	var user string = user_prompt()
	var password string = password_prompt()

	// Making HTTP GET request
	resp, err := http.Get("https://fw01.zmacharia.local/api/?type=keygen&user=" + user + "&password=" + password)
	if err != nil {
		log.Fatalln(err)
	}
	defer resp.Body.Close()

	//Reading the response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}

	// Convert response to string bytes
	sb := string(body)

	// Remove characters leading the API key
	rm_response_head := strings.TrimLeft(sb, "<response status= 'success'><result><key>")
	if err != nil {
		log.Fatalln(err)
	}

	// Removing characters trailing the API key
	api_key := strings.TrimRight(rm_response_head, "</key></result></response>")
	if err != nil {
		log.Fatalln(err)
	}

	fmt.Println(api_key)
}

func user_prompt() string {

	// Displaying text on screen
	fmt.Println("Username: ")
	var user string

	//Taking user input
	fmt.Scanln(&user)

	return user
}

func password_prompt() string {

	// Displaying text on screen
	fmt.Println("Password: ")
	var password string

	//Taking user input
	fmt.Scanln(&password)

	return password
}
