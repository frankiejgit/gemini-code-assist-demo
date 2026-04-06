import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 * LEGACY SERVICE FOR SENSOR DATA PROCESSING
 * 
 * This service reads sensor data from a legacy CSV format and calculates anomaly scores.
 * It uses older Java patterns (pre-Java 11/17/21).
 */
public class StationDataProcessor {

    private String dataFilePath;

    public StationDataProcessor(String dataFilePath) {
        this.dataFilePath = dataFilePath;
    }

    public List<StationAnomaly> processAnomalies() {
        List<StationAnomaly> anomalies = new ArrayList<StationAnomaly>();
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(dataFilePath));
            String line;
            // Skip header
            reader.readLine();
            
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length >= 4) {
                    String id = parts[0];
                    double uptime = Double.parseDouble(parts[1]);
                    int count = Integer.parseInt(parts[2]);
                    int calibrationAge = Integer.parseInt(parts[3]);
                    
                    double score = calculateLegacyAnomalyScore(uptime, count, calibrationAge);
                    anomalies.add(new StationAnomaly(id, score));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        // Sort by anomaly score descending using anonymous inner class
        Collections.sort(anomalies, new Comparator<StationAnomaly>() {
            @Override
            public int compare(StationAnomaly o1, StationAnomaly o2) {
                return Double.compare(o2.getScore(), o1.getScore());
            }
        });

        return anomalies;
    }

    private double calculateLegacyAnomalyScore(double uptime, int anomalyCount, int calAge) {
        // Complex legacy logic with magic numbers
        double score = (anomalyCount / (uptime + 1.0)) * 1000.0;
        if (calAge > 365) {
            score *= 1.25;
        }
        return score;
    }

    public static void main(String[] args) {
        StationDataProcessor processor = new StationDataProcessor("data/sensor_readings.csv");
        List<StationAnomaly> results = processor.processAnomalies();
        for (StationAnomaly a : results) {
            System.out.println("Station: " + a.getStationId() + " - Anomaly Score: " + a.getScore());
        }
    }
}

class StationAnomaly {
    private String stationId;
    private double score;

    public StationAnomaly(String stationId, double score) {
        this.stationId = stationId;
        this.score = score;
    }

    public String getStationId() {
        return stationId;
    }

    public double getScore() {
        return score;
    }
}
