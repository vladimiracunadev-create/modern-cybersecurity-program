/**
 * PartScreen.js — Listado de las clases de una parte.
 *
 * Segundo nivel de navegación: el Home muestra las 19 partes y esta pantalla
 * despliega las clases de la parte elegida (entre 10 y 30 según la parte), con
 * un buscador por número, título o tema.
 */

import React, { useState, useCallback, useMemo } from 'react';
import {
  View,
  Text,
  TextInput,
  FlatList,
  StyleSheet,
  SafeAreaView,
} from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { PARTS, classesForPart } from '../data/classes';
import ClassCard from '../components/ClassCard';
import { getProgress } from '../utils/progress';
import { colors, spacing, radius, fontSize, fontWeight } from '../theme';

const normalize = (value) =>
  String(value)
    .toLowerCase()
    .normalize('NFD')
    .replace(/\p{Diacritic}/gu, '');

export default function PartScreen({ route, navigation }) {
  const { partId } = route.params;
  const part = useMemo(() => PARTS.find((item) => item.id === partId), [partId]);
  const classes = useMemo(() => classesForPart(partId), [partId]);

  const [completedIds, setCompletedIds] = useState(new Set());
  const [query, setQuery] = useState('');

  useFocusEffect(
    useCallback(() => {
      let active = true;
      getProgress().then((progress) => {
        if (active) setCompletedIds(progress);
      });
      return () => {
        active = false;
      };
    }, [])
  );

  const filtered = useMemo(() => {
    const term = normalize(query.trim());
    if (!term) return classes;
    return classes.filter(
      (item) =>
        normalize(item.title).includes(term) ||
        String(item.number).includes(term) ||
        (item.topics || []).some((topic) => normalize(topic).includes(term))
    );
  }, [classes, query]);

  const completedCount = classes.reduce(
    (total, item) => (completedIds.has(item.id) ? total + 1 : total),
    0
  );
  const progressPercent = classes.length > 0 ? (completedCount / classes.length) * 100 : 0;

  const handleClassPress = (classItem) => {
    navigation.navigate('Class', {
      classData: classItem,
      classTitle: `Clase ${classItem.number}`,
    });
  };

  if (!part) {
    return (
      <SafeAreaView style={styles.safeArea}>
        <View style={styles.emptyBox}>
          <Text style={styles.emptyText}>No se encontró esta parte del programa.</Text>
        </View>
      </SafeAreaView>
    );
  }

  const renderHeader = () => (
    <View style={styles.headerContainer}>
      <Text style={styles.partTitle}>{part.number}. {part.title}</Text>
      <Text style={styles.partSubtitle}>{part.subtitle}</Text>

      <View style={styles.progressRow}>
        <View style={styles.progressTrack}>
          <View style={[styles.progressFill, { width: `${progressPercent}%` }]} />
        </View>
        <Text style={styles.progressText}>{completedCount}/{classes.length}</Text>
      </View>

      <TextInput
        style={styles.searchInput}
        value={query}
        onChangeText={setQuery}
        placeholder="Buscar por número, título o tema"
        placeholderTextColor={colors.textMuted}
        autoCorrect={false}
        clearButtonMode="while-editing"
      />

      {query.trim() ? (
        <Text style={styles.resultsText}>
          {filtered.length} {filtered.length === 1 ? 'resultado' : 'resultados'}
        </Text>
      ) : null}
    </View>
  );

  const renderEmpty = () => (
    <View style={styles.emptyBox}>
      <Text style={styles.emptyText}>Ninguna clase coincide con “{query.trim()}”.</Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.safeArea}>
      <FlatList
        data={filtered}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <ClassCard
            classData={item}
            completed={completedIds.has(item.id)}
            onPress={() => handleClassPress(item)}
          />
        )}
        ListHeaderComponent={renderHeader}
        ListEmptyComponent={renderEmpty}
        contentContainerStyle={styles.listContent}
        showsVerticalScrollIndicator={false}
        initialNumToRender={8}
        windowSize={10}
        removeClippedSubviews
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: colors.bg },
  listContent: { paddingBottom: spacing.xl },
  headerContainer: {
    paddingHorizontal: spacing.md,
    paddingTop: spacing.md,
    paddingBottom: spacing.sm,
  },
  partTitle: {
    color: colors.text,
    fontSize: 22,
    fontWeight: fontWeight.bold,
    marginBottom: 2,
  },
  partSubtitle: {
    color: colors.textMuted,
    fontSize: fontSize.sm,
    lineHeight: 19,
    marginBottom: spacing.md,
  },
  progressRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    marginBottom: spacing.md,
  },
  progressTrack: {
    flex: 1,
    height: 6,
    backgroundColor: colors.bgMuted,
    borderRadius: radius.sm,
    overflow: 'hidden',
  },
  progressFill: { height: '100%', backgroundColor: colors.accent, borderRadius: radius.sm },
  progressText: { color: colors.textMuted, fontSize: fontSize.xs, fontWeight: fontWeight.medium },
  searchInput: {
    backgroundColor: colors.bgInput,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: radius.md,
    paddingHorizontal: spacing.md,
    paddingVertical: 10,
    color: colors.text,
    fontSize: fontSize.sm,
  },
  resultsText: { color: colors.textMuted, fontSize: fontSize.xs, marginTop: spacing.sm },
  emptyBox: { padding: spacing.xl, alignItems: 'center' },
  emptyText: { color: colors.textMuted, fontSize: fontSize.sm, textAlign: 'center' },
});
