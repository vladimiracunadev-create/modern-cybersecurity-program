/**
 * ClassScreen.js — La clase completa, sin conexión.
 *
 * Dos pestañas, alimentadas por los bloques que el generador embebe en
 * src/data/classes.js a partir del README:
 *   Teoría   → objetivo, resultados, temas, explicación en profundidad,
 *              definiciones y glosario
 *   Práctica → herramientas y preparación, laboratorio guiado, ejercicios,
 *              reto verificable, errores comunes, preguntas y referencias
 *
 * Hasta la versión anterior aquí solo cabía un resumen recortado y había que
 * salir al sitio para leer la clase de verdad; ahora el texto completo viaja en
 * el APK. Si un catálogo antiguo no trae ``content``, se cae al resumen de
 * siempre en vez de dejar la pantalla vacía.
 *
 * Los botones inferiores siguen abriendo la clase en el sitio (con sus
 * diagramas dibujados) y su fuente en GitHub.
 */

import React, { useEffect, useState } from 'react';
import {
  Alert,
  Linking,
  SafeAreaView,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import ClassContent from '../components/ClassContent';
import { isClassCompleted, removeProgress, saveProgress } from '../utils/progress';
import { colors, spacing, radius, fontSize, fontWeight, levelColor } from '../theme';

const openUrl = async (url, label) => {
  if (!url) return;
  try {
    const canOpen = await Linking.canOpenURL(url);
    if (canOpen) {
      await Linking.openURL(url);
      return;
    }
  } catch (error) {
    // cae al Alert
  }
  Alert.alert(
    `No se pudo abrir ${label}`,
    'Verifica que tengas conexión a internet y un navegador disponible.',
    [{ text: 'OK' }]
  );
};

export default function ClassScreen({ route }) {
  const { classData } = route.params;

  const outcomes = classData.outcomes ?? [];
  const topics = classData.topics ?? [];
  const definitions = classData.definitions ?? [];
  const tools = classData.tools ?? [];
  const exercises = classData.exercises ?? [];
  const lab = classData.lab ?? '';

  // Clase completa embebida. Un catálogo anterior a esta versión no la trae.
  const theoryBlocks = classData.content?.theory ?? [];
  const practiceBlocks = classData.content?.practice ?? [];
  const hasFullContent = theoryBlocks.length > 0 || practiceBlocks.length > 0;

  const [activeTab, setActiveTab] = useState('theory');
  const [completed, setCompleted] = useState(false);

  useEffect(() => {
    isClassCompleted(classData.id).then(setCompleted);
  }, [classData.id]);

  const handleToggleCompleted = async () => {
    if (completed) {
      await removeProgress(classData.id);
      setCompleted(false);
      return;
    }
    await saveProgress(classData.id);
    setCompleted(true);
  };

  const TheoryTab = () =>
    hasFullContent ? (
      <ScrollView style={styles.tabContent} showsVerticalScrollIndicator={false}>
        <ClassContent
          blocks={theoryBlocks}
          empty="Esta clase no trae parte teórica embebida. Ábrela en el sitio."
        />
        <View style={styles.bottomSpacer} />
      </ScrollView>
    ) : (
      <SummaryTheoryTab />
    );

  // Resumen de respaldo: solo se usa si el catálogo embebido es antiguo.
  const SummaryTheoryTab = () => (
    <ScrollView style={styles.tabContent} showsVerticalScrollIndicator={false}>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Objetivo</Text>
        <Text style={styles.cardText}>{classData.theory || classData.description}</Text>
      </View>

      {outcomes.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Resultados de aprendizaje</Text>
          {outcomes.map((item, index) => (
            <View key={`outcome-${index}`} style={styles.rowItem}>
              <View style={styles.bullet} />
              <Text style={styles.rowText}>{item}</Text>
            </View>
          ))}
        </View>
      )}

      {topics.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Temas de esta clase</Text>
          {topics.map((item, index) => (
            <View key={`topic-${index}`} style={styles.rowItem}>
              <View style={[styles.bullet, styles.bulletBlue]} />
              <Text style={styles.rowText}>{item}</Text>
            </View>
          ))}
        </View>
      )}

      {definitions.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Definiciones clave</Text>
          {definitions.map((item, index) => (
            <View key={`def-${index}`} style={styles.rowItem}>
              <View style={[styles.bullet, styles.bulletBlue]} />
              <Text style={styles.rowText}>{item}</Text>
            </View>
          ))}
        </View>
      )}

      {tools.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Herramientas y preparación</Text>
          {tools.map((item, index) => (
            <View key={`tool-${index}`} style={styles.rowItem}>
              <View style={styles.bullet} />
              <Text style={styles.rowText}>{item}</Text>
            </View>
          ))}
        </View>
      )}

      <View style={styles.bottomSpacer} />
    </ScrollView>
  );

  const PracticeTab = () =>
    hasFullContent ? (
      <ScrollView style={styles.tabContent} showsVerticalScrollIndicator={false}>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Antes de empezar</Text>
          <Text style={styles.cardText}>
            Monta siempre un entorno propio y aislado. Todo lo ofensivo de este programa es para
            laboratorios tuyos o sistemas con permiso explícito.
          </Text>
        </View>
        <ClassContent
          blocks={practiceBlocks}
          empty="Esta clase es sobre todo conceptual: su práctica está en la pestaña de teoría."
        />
        <View style={styles.bottomSpacer} />
      </ScrollView>
    ) : (
      <SummaryPracticeTab />
    );

  const SummaryPracticeTab = () => (
    <ScrollView style={styles.tabContent} showsVerticalScrollIndicator={false}>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Cómo practicar</Text>
        <Text style={styles.cardText}>
          Monta siempre un entorno propio y aislado. Abre la clase completa en el sitio para
          seguir el laboratorio paso a paso con sus comandos y capturas.
        </Text>
      </View>

      {lab ? (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Laboratorio guiado</Text>
          <Text style={styles.cardText}>{lab}</Text>
        </View>
      ) : null}

      {exercises.map((exercise, index) => (
        <View key={`${classData.id}-ex-${index}`} style={styles.exerciseCard}>
          <Text style={styles.exerciseNumber}>Ejercicio {index + 1}</Text>
          <Text style={styles.exerciseText}>{exercise}</Text>
        </View>
      ))}

      {!lab && exercises.length === 0 ? (
        <View style={styles.card}>
          <Text style={styles.cardText}>
            Esta clase es sobre todo conceptual. Abre la clase completa para ver la práctica.
          </Text>
        </View>
      ) : null}

      <View style={styles.bottomSpacer} />
    </ScrollView>
  );

  return (
    <SafeAreaView style={styles.safeArea}>
      <View style={styles.headerCard}>
        <View style={styles.headerRow}>
          <View style={styles.numberBadge}>
            <Text style={styles.numberBadgeText}>{classData.number}</Text>
          </View>
          <View style={styles.headerTextBlock}>
            <Text style={styles.title}>{classData.title}</Text>
            <Text style={styles.description}>{classData.description}</Text>
            <View style={styles.badgesRow}>
              <View style={[styles.levelBadge, { backgroundColor: levelColor(classData.level) }]}>
                <Text style={styles.levelBadgeText}>{classData.level}</Text>
              </View>
              <View style={styles.durationBadge}>
                <Text style={styles.durationText}>{classData.duration}</Text>
              </View>
            </View>
          </View>
        </View>
      </View>

      <View style={styles.tabBar}>
        <TouchableOpacity
          style={[styles.tabButton, activeTab === 'theory' && styles.tabButtonActive]}
          onPress={() => setActiveTab('theory')}
        >
          <Text style={[styles.tabButtonText, activeTab === 'theory' && styles.tabButtonTextActive]}>
            Teoría
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tabButton, activeTab === 'practice' && styles.tabButtonActive]}
          onPress={() => setActiveTab('practice')}
        >
          <Text style={[styles.tabButtonText, activeTab === 'practice' && styles.tabButtonTextActive]}>
            Práctica
          </Text>
        </TouchableOpacity>
      </View>

      <View style={styles.contentArea}>
        {activeTab === 'theory' ? <TheoryTab /> : <PracticeTab />}
      </View>

      <View style={styles.bottomBar}>
        <TouchableOpacity
          style={[styles.completeButton, completed && styles.completeButtonDone]}
          onPress={handleToggleCompleted}
        >
          <Text style={styles.completeButtonText}>
            {completed ? 'Completada' : 'Completar'}
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.openButton}
          onPress={() => openUrl(classData.siteUrl, 'el sitio')}
        >
          <Text style={styles.openButtonText}>Abrir la clase</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.githubButton}
          onPress={() => openUrl(classData.githubUrl, 'GitHub')}
        >
          <Text style={styles.githubButtonText}>GitHub</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: colors.bg },
  headerCard: {
    backgroundColor: colors.bgCard,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
    paddingHorizontal: 16,
    paddingVertical: 14,
  },
  headerRow: { flexDirection: 'row', gap: 12, alignItems: 'flex-start' },
  numberBadge: {
    width: 46,
    height: 46,
    borderRadius: 12,
    backgroundColor: colors.accent,
    alignItems: 'center',
    justifyContent: 'center',
  },
  numberBadgeText: { color: '#04110a', fontSize: 16, fontWeight: '800', fontFamily: 'monospace' },
  headerTextBlock: { flex: 1, minWidth: 0 },
  title: { color: colors.text, fontSize: 18, fontWeight: '700', marginBottom: 4 },
  description: { color: colors.textMuted, fontSize: 13, lineHeight: 19, marginBottom: 8 },
  badgesRow: { flexDirection: 'row', gap: 8, flexWrap: 'wrap' },
  levelBadge: { paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  levelBadgeText: { color: '#04110a', fontSize: 11, fontWeight: '800' },
  durationBadge: {
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
    backgroundColor: colors.bgMuted,
  },
  durationText: { color: colors.textMuted, fontSize: 11, fontWeight: '600' },
  tabBar: {
    flexDirection: 'row',
    backgroundColor: colors.bgCard,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  tabButton: { flex: 1, paddingVertical: 12, alignItems: 'center' },
  tabButtonActive: { borderBottomWidth: 2, borderBottomColor: colors.accent },
  tabButtonText: { color: colors.textMuted, fontSize: 14, fontWeight: '600' },
  tabButtonTextActive: { color: colors.accent },
  contentArea: { flex: 1 },
  tabContent: { flex: 1, paddingHorizontal: 16, paddingTop: 16 },
  card: {
    backgroundColor: colors.bgCard,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: colors.border,
    padding: 14,
    marginBottom: 16,
  },
  cardTitle: { color: colors.text, fontSize: 15, fontWeight: '700', marginBottom: 10 },
  cardText: { color: colors.textMuted, fontSize: 14, lineHeight: 22 },
  rowItem: { flexDirection: 'row', alignItems: 'flex-start', gap: 10, marginBottom: 8 },
  bullet: { width: 8, height: 8, borderRadius: 4, backgroundColor: colors.accent, marginTop: 6 },
  bulletBlue: { backgroundColor: colors.accentBlue },
  rowText: { flex: 1, minWidth: 0, color: colors.textMuted, lineHeight: 21, fontSize: 14 },
  chipsWrap: { flexDirection: 'row', flexWrap: 'wrap', gap: 8 },
  chip: {
    backgroundColor: colors.bgMuted,
    borderRadius: 999,
    borderWidth: 1,
    borderColor: colors.border,
    paddingHorizontal: 10,
    paddingVertical: 6,
  },
  chipText: { color: colors.text, fontSize: 12 },
  exerciseCard: { marginBottom: 20 },
  exerciseNumber: {
    color: colors.accentBlue,
    fontSize: 11,
    fontWeight: '700',
    marginBottom: 4,
    textTransform: 'uppercase',
  },
  exerciseText: { color: colors.textMuted, fontSize: 14, lineHeight: 21 },
  bottomBar: {
    flexDirection: 'row',
    gap: 8,
    padding: 12,
    backgroundColor: colors.bgCard,
    borderTopWidth: 1,
    borderTopColor: colors.border,
  },
  completeButton: {
    flex: 1.2,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: colors.border,
    backgroundColor: colors.bgMuted,
    paddingVertical: 13,
    alignItems: 'center',
  },
  completeButtonDone: { backgroundColor: '#0b1d12', borderColor: colors.accent },
  completeButtonText: { color: colors.text, fontWeight: '700', fontSize: 13 },
  openButton: {
    flex: 1.3,
    borderRadius: 10,
    backgroundColor: colors.accent,
    paddingVertical: 13,
    alignItems: 'center',
  },
  openButtonText: { color: '#04110a', fontWeight: '800', fontSize: 13 },
  githubButton: {
    flex: 1,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: colors.accentBlue,
    paddingVertical: 13,
    alignItems: 'center',
  },
  githubButtonText: { color: colors.accentBlue, fontWeight: '700', fontSize: 13 },
  bottomSpacer: { height: 24 },
});
