import { StyleSheet, TextInput, View, Text, Button } from 'react-native';
import { useState } from 'react';

let ipv4 = "your-ipv4";
port = 5000;

export default function App() {

  const [text, updateText] = useState('');


  return (
    <View style={styles.container}>
      <TextInput
        onChangeText={updateText}
        value={text}
        placeholder="Enter prompt..."
      />

      <Button title={"Send request"} onPress={() => requestImage(text)} />
    </View>

  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

async function requestImage(prompt) {
  let image = await fetch(`http://${ipv4}:${port}`, {
      headers: { "prompt": prompt }
    }
  ).then((response) => response.json())

  console.log(image)
  
  
}
