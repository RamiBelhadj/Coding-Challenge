package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"time"
)

type DBData struct {
	Data struct {
		DataPoints []struct {
			MessageID     string    `json:"message_id"`
			AccountID     string    `json:"account_id"`
			CreatedAt     time.Time `json:"created_at"`
			ID            string    `json:"id"`
			DataPointType string    `json:"data_point_type"`
		} `json:"data_points"`
	} `json:"data"`
}

func getDataPoints() DBData {
	jsonFile, err := os.Open("../mock-data.json")
	if err != nil {
		fmt.Println(err)
	}
	defer jsonFile.Close()
	byteValue, _ := ioutil.ReadAll(jsonFile)
	var dbData DBData
	err = json.Unmarshal(byteValue, &dbData)
	if err != nil {
		panic(err)
	}
	return dbData
}

type Cache struct {
}

func main() {
}
