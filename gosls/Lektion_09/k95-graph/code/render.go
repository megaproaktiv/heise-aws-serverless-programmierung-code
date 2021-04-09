package k95graph

import (
	"os"
	"github.com/wcharczuk/go-chart/v2"
)

// Render - erzeuge Diagramm mit den Gewichtswerten
func Render(weights []Weight, fileName string) {

	values := make([]chart.Value,0)

	for _, weight := range weights {
		var v = chart.Value{
			Label: weight.Date,
			Value: weight.Hectogram / 10,
		}
        values = append(values, v)
    }

	graph := chart.BarChart{
		Title: "Gewichtsverlauf",
		Background: chart.Style{
			Padding: chart.Box{
				Top: 40,
			},
			
		},
		Height:   512,
		BarWidth: 60,
		Bars: values,
	}

	

	f, _ := os.Create(fileName)
	defer f.Close()
	graph.Render(chart.PNG, f)
}
