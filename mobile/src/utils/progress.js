// ============================================================
// PROGRESO DEL ALUMNO (persistente, local)
// Usa AsyncStorage para recordar qué clases se marcaron como completadas.
// Los datos sobreviven al cierre de la app y no salen del dispositivo.
// ============================================================

import AsyncStorage from '@react-native-async-storage/async-storage';

const PROGRESS_KEY = '@modern_cybersecurity_program:progress';

/** Marca una clase como completada y persiste. Devuelve el Set actualizado. */
export const saveProgress = async (classId) => {
  try {
    const current = await getProgress();
    current.add(classId);
    await AsyncStorage.setItem(PROGRESS_KEY, JSON.stringify(Array.from(current)));
    return current;
  } catch (error) {
    console.error('Error al guardar progreso:', error);
    return new Set([classId]);
  }
};

/** Set con los IDs de clases completadas (vacío si no hay nada guardado). */
export const getProgress = async () => {
  try {
    const jsonValue = await AsyncStorage.getItem(PROGRESS_KEY);
    if (jsonValue === null) return new Set();
    return new Set(JSON.parse(jsonValue));
  } catch (error) {
    console.error('Error al leer progreso:', error);
    return new Set();
  }
};

/** Des-marca una clase como completada. */
export const removeProgress = async (classId) => {
  try {
    const current = await getProgress();
    current.delete(classId);
    await AsyncStorage.setItem(PROGRESS_KEY, JSON.stringify(Array.from(current)));
    return current;
  } catch (error) {
    console.error('Error al eliminar progreso:', error);
    return await getProgress();
  }
};

/** true si la clase está marcada como completada. */
export const isClassCompleted = async (classId) => {
  const progress = await getProgress();
  return progress.has(classId);
};

/** Borra todo el progreso del alumno. */
export const clearProgress = async () => {
  try {
    await AsyncStorage.removeItem(PROGRESS_KEY);
  } catch (error) {
    console.error('Error al limpiar progreso:', error);
  }
};
