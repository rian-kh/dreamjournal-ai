import { StyleSheet, TextInput, View, Text, Button, Image } from 'react-native';
import { useState } from 'react';

let ipv4 = "your-ipv4";
port = 5000;


export default function App() {

  const [text, updateText] = useState('');
  const [imageURL, updateImage] = useState(null);

  return (
    <View style={styles.container}>
      <TextInput
        onChangeText={updateText}
        value={text}
        placeholder="Enter prompt..."
      />

      <Button title={"Generate image"} onPress={async () => updateImage(await requestImage(text))} />
      {imageURL && <Image source={{ uri: imageURL }} style={{ height: 500, width: 500 }} />}
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
  ).then((response) => response.blob())

  let url = URL.createObjectURL(image);
  return url;

}
