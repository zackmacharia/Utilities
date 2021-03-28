package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"os/exec"
	"strings"
)

func main() {
	fmt.Println("This programs checks the hash of a file and compares to a user entered hash")
	filename := getFileName()
	hash := userHash()
	hashes := getHashes(filename)
	if hash == hashes[0] {
		fmt.Printf("Matched -> MD5: %s \n", hashes[0])
	} else if hash == hashes[1] {
		fmt.Printf("Matched -> SHA1: %s \n", hashes[1])
	} else if hash == hashes[2] {
		fmt.Printf("Matched -> SHA256: %s \n", hashes[2])
	}
}

func getFileName() string {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter File's Fullpath: ")
	scanner.Scan()
	entry := scanner.Text()
	return entry
}

func userHash() string {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter the expected hash output: ")
	scanner.Scan()
	entry := scanner.Text()
	return entry
}

func getHashes(filename string) []string {
	hashes := []string{
		getMd5(filename),
		getSha1(filename),
		getSha256(filename)}
	return hashes
}

func getMd5(filename string) string {
	out, err := exec.Command("md5", filename).Output()
	if err != nil {
		log.Fatal(err)
	}
	outStr := string(out)
	outArr := strings.Fields(outStr)
	hash := outArr[3]
	return hash
}

func getSha1(filename string) string {
	out, err := exec.Command("shasum", "-a", "1", filename).Output()
	if err != nil {
		log.Fatal(err)
	}
	outStr := string(out)
	outArr := strings.Fields(outStr)
	hash := outArr[0]
	return hash
}

func getSha256(filename string) string {
	out, err := exec.Command("shasum", "-a", "256", filename).Output()
	if err != nil {
		log.Fatal(err)
	}
	outStr := string(out)
	outArr := strings.Fields(outStr)
	hash := outArr[0]
	return hash
}
