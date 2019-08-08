import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class readfromcsvtoarray {

    public static void main(String[] args) {
	
	BufferedReader csvReader = null;
        try {

		csvReader = new BufferedReader(new FileReader("stu.csv"));
		String row = null;
		String[] data = null;
		int i = 0;
		while ((row = csvReader.readLine()) != null) {
    			data[i] = row;
			i++;
   		// do something with the data
		System.out.println(data[0]);
		}
		

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (csvReader != null) {
                try {
                    csvReader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }


    }

}

