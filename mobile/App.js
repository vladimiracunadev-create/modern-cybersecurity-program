/**
 * App.js — Punto de entrada de la app "Ciberseguridad Moderna".
 *
 * Configura:
 *   - NavigationContainer con tema oscuro propio
 *   - Stack Navigator con las pantallas Home / Part / Class
 *   - SafeAreaProvider para respetar notches y barras del sistema
 */

import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { NavigationContainer, DarkTheme } from '@react-navigation/native';
import AppNavigator from './src/navigation/AppNavigator';
import { colors } from './src/theme';

// Tema oscuro personalizado para la navegación.
const ProgramTheme = {
  ...DarkTheme,
  colors: {
    ...DarkTheme.colors,
    primary: colors.accent,
    background: colors.bg,
    card: colors.bgCard,
    text: colors.text,
    border: colors.border,
    notification: colors.accent,
  },
};

export default function App() {
  return (
    <SafeAreaProvider>
      <StatusBar style="light" backgroundColor={colors.bg} />
      <NavigationContainer theme={ProgramTheme}>
        <AppNavigator />
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
