import React, { Component } from 'react';
import { AnimatedCircularProgress } from 'react-native-circular-progress';
import ActionButton from 'react-native-action-button';
import Icon from 'react-native-vector-icons/Ionicons';
import AwesomeButton from 'react-native-awesome-button';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View
} from 'react-native';

export default class SmartPlant extends Component {

  constructor(props) {
    super(props)
    this.state = {
        buttonState: 'idle'
    }
    this.logIn = this.logIn.bind(this)
  }

  logIn() {
    this.setState({ buttonState: 'busy' })
    setTimeout(() => {
      this.setState({ buttonState: 'success' })
    }, 2000);
  }

  getData() {
    console.log("getData")
  }
  render() {
    const fill = 70
    return (
      <View style={styles.container}>
        <Text style={styles.title}>
          SmartPlant
        </Text>
        <Text style={styles.label}>
          現在の湿度
        </Text>
        <AnimatedCircularProgress
          size={200}
          width={3}
          fill={fill}
          tintColor="#00e0ff"
          backgroundColor="#3d5875">
          {
            (fill) => (
              <Text style={styles.points}>
                {Math.round(fill)}
              </Text>
            )
          }
        </AnimatedCircularProgress>
        <View style={styles.getDataView}>
          <AwesomeButton
            backgroundStyle={styles.getDataButtonBackground}
            labelStyle={styles.getDataButtonLabel}
            transitionDuration={200}
            states={{
              idle: {
                text: 'データを取得する',
                onPress: this.logIn,
                backgroundColor: '#1155DD',
              },
              busy: {
                text: '読み込み中',
                backgroundColor: '#002299',
                spinner: true,
              },
              success: {
                text: '完了しました',
                backgroundColor: '#339944'
              }
            }}
            buttonState={this.state.buttonState}
            />
        </View>
        <ActionButton
          buttonColor="rgba(231,76,60,1)"
          icon={<Icon name="md-settings" style={styles.actionButtonIcon} />}>
          <ActionButton.Item buttonColor='#9b59b6' title="Scan Device" onPress={() => console.log("notes tapped!")}>
            <Icon name="md-search" style={styles.actionButtonIcon} />
          </ActionButton.Item>
          <ActionButton.Item buttonColor='#3498db' title="Notifications" onPress={() => {}}>
            <Icon name="md-notifications" style={styles.actionButtonIcon} />
          </ActionButton.Item>
        </ActionButton>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#152d44',
    padding: 50
  },
  title: {
    fontSize: 30,
    color: "#fff",
    textAlign: 'center',
    marginVertical: 20,
  },
  label: {
    fontSize: 20,
    color: "#fff",
    textAlign: 'center',
    marginVertical: 10,
  },
  points: {
    backgroundColor: 'transparent',
    position: 'absolute',
    top: 72,
    left: 56,
    width: 90,
    textAlign: 'center',
    color: '#7591af',
    fontSize: 50,
    fontWeight: "100"
  },
  getDataView: {
    marginTop: 20,
    height: 60,
    width: 200
  },
  getDataButtonBackground: {
    height: 40,
    borderRadius: 5
  },
  getDataButtonLabel: {
    color: 'white'
  },
  actionButtonIcon: {
    fontSize: 20,
    height: 22,
    color: 'white',
  }
});

AppRegistry.registerComponent('SmartPlant', () => SmartPlant);
