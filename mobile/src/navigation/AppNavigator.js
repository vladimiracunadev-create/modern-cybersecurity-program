/**
 * AppNavigator.js — Rutas de la app.
 *
 *   Home  → las 19 partes del programa, con progreso global
 *   Part  → las clases de una parte, con buscador
 *   Class → detalle de una clase (teoría + práctica + enlaces)
 *   Resource → recurso transversal completo, disponible sin conexión
 */

import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/HomeScreen';
import PartScreen from '../screens/PartScreen';
import ClassScreen from '../screens/ClassScreen';
import ResourceScreen from '../screens/ResourceScreen';
import { colors } from '../theme';

const Stack = createStackNavigator();

const headerOptions = {
  headerStyle: {
    backgroundColor: colors.bgCard,
    elevation: 0,
    shadowOpacity: 0,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  headerTintColor: colors.text,
  headerTitleStyle: { fontWeight: '700', fontSize: 17 },
  headerBackTitleVisible: false,
};

export default function AppNavigator() {
  return (
    <Stack.Navigator initialRouteName="Home" screenOptions={headerOptions}>
      <Stack.Screen
        name="Home"
        component={HomeScreen}
        options={{ title: 'Ciberseguridad Moderna' }}
      />
      <Stack.Screen
        name="Part"
        component={PartScreen}
        options={({ route }) => ({ title: route.params?.partTitle ?? 'Parte' })}
      />
      <Stack.Screen
        name="Class"
        component={ClassScreen}
        options={({ route }) => ({ title: route.params?.classTitle ?? 'Clase' })}
      />
      <Stack.Screen
        name="Resource"
        component={ResourceScreen}
        options={({ route }) => ({ title: route.params?.resourceTitle ?? 'Recurso' })}
      />
    </Stack.Navigator>
  );
}
