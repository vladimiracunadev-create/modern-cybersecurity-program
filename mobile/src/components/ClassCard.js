// ============================================================
// COMPONENTE: ClassCard — tarjeta de clase en la lista de una parte.
// ============================================================

import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { colors, spacing, radius, fontSize, fontWeight, levelColor } from '../theme';

const ClassCard = ({ classData, completed, onPress }) => {
  const { number, title, description, topics, duration, level } = classData;
  const lvlColor = levelColor(level);
  const chips = (topics || []).slice(0, 3);

  return (
    <TouchableOpacity
      style={[styles.card, completed && styles.cardCompleted]}
      onPress={onPress}
      activeOpacity={0.85}
    >
      {completed && (
        <View style={styles.completedBadge}>
          <Text style={styles.completedBadgeText}>OK</Text>
        </View>
      )}

      <View style={styles.headerRow}>
        <View style={[styles.numberBadge, completed && styles.numberBadgeCompleted]}>
          <Text style={styles.numberText}>{String(number).padStart(3, '0')}</Text>
        </View>
        <View style={styles.titleArea}>
          <Text style={[styles.title, completed && styles.titleCompleted]} numberOfLines={2}>
            {title}
          </Text>
          <View style={styles.badgesRow}>
            <View style={[styles.levelBadge, { borderColor: lvlColor }]}>
              <Text style={[styles.levelText, { color: lvlColor }]}>{level}</Text>
            </View>
            <View style={styles.durationBadge}>
              <Text style={styles.durationText}>{duration}</Text>
            </View>
          </View>
        </View>
      </View>

      <Text style={styles.description} numberOfLines={2}>{description}</Text>

      {chips.length > 0 && (
        <View style={styles.topicsRow}>
          {chips.map((topic, index) => (
            <View key={index} style={styles.topicChip}>
              <Text style={styles.topicText} numberOfLines={1}>{topic}</Text>
            </View>
          ))}
          {topics.length > 3 && (
            <View style={styles.topicChipMore}>
              <Text style={styles.topicMoreText}>+{topics.length - 3}</Text>
            </View>
          )}
        </View>
      )}

      <View style={styles.footer}>
        {completed && (
          <View style={styles.completedLabel}>
            <Text style={styles.completedLabelText}>Completada</Text>
          </View>
        )}
        <TouchableOpacity
          style={[styles.button, completed && styles.buttonCompleted]}
          onPress={onPress}
          activeOpacity={0.8}
        >
          <Text style={[styles.buttonText, completed && styles.buttonTextCompleted]}>
            {completed ? 'Repasar' : 'Ver clase'}
          </Text>
        </TouchableOpacity>
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: colors.bgCard,
    borderRadius: radius.lg,
    padding: spacing.md,
    marginHorizontal: spacing.md,
    marginVertical: spacing.sm,
    borderWidth: 1,
    borderColor: colors.border,
    elevation: 2,
  },
  cardCompleted: { borderColor: `${colors.accent}55`, backgroundColor: '#13251a' },
  completedBadge: {
    position: 'absolute',
    top: spacing.sm,
    right: spacing.sm,
    width: 24,
    height: 24,
    borderRadius: radius.full,
    backgroundColor: colors.accent,
    alignItems: 'center',
    justifyContent: 'center',
    zIndex: 1,
  },
  completedBadgeText: { color: '#04110a', fontSize: fontSize.xs, fontWeight: fontWeight.bold },
  headerRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: spacing.sm,
    gap: spacing.md,
  },
  numberBadge: {
    width: 44,
    height: 44,
    borderRadius: radius.md,
    backgroundColor: `${colors.accent}22`,
    borderWidth: 1.5,
    borderColor: colors.accent,
    alignItems: 'center',
    justifyContent: 'center',
    flexShrink: 0,
  },
  numberBadgeCompleted: { backgroundColor: colors.accent, borderColor: colors.accent },
  numberText: {
    color: colors.accent,
    fontSize: fontSize.sm,
    fontWeight: fontWeight.bold,
    fontFamily: 'monospace',
  },
  titleArea: { flex: 1, minWidth: 0 },
  title: {
    color: colors.text,
    fontSize: fontSize.lg,
    fontWeight: fontWeight.bold,
    marginBottom: spacing.xs,
    lineHeight: 22,
  },
  titleCompleted: { color: colors.accent },
  badgesRow: { flexDirection: 'row', gap: spacing.sm, flexWrap: 'wrap' },
  levelBadge: {
    paddingHorizontal: spacing.sm,
    paddingVertical: 2,
    borderRadius: radius.full,
    borderWidth: 1,
  },
  levelText: { fontSize: fontSize.xs, fontWeight: fontWeight.medium },
  durationBadge: {
    paddingHorizontal: spacing.sm,
    paddingVertical: 2,
    borderRadius: radius.full,
    backgroundColor: colors.bgMuted,
  },
  durationText: { color: colors.textMuted, fontSize: fontSize.xs },
  description: {
    color: colors.textMuted,
    fontSize: fontSize.sm,
    lineHeight: 20,
    marginBottom: spacing.md,
  },
  topicsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: spacing.xs,
    marginBottom: spacing.md,
  },
  topicChip: {
    backgroundColor: `${colors.accentBlue}22`,
    borderWidth: 1,
    borderColor: `${colors.accentBlue}55`,
    paddingHorizontal: spacing.sm,
    paddingVertical: 3,
    borderRadius: radius.full,
    maxWidth: 180,
  },
  topicText: { color: colors.accentBlue, fontSize: fontSize.xs },
  topicChipMore: {
    backgroundColor: colors.bgMuted,
    paddingHorizontal: spacing.sm,
    paddingVertical: 3,
    borderRadius: radius.full,
  },
  topicMoreText: { color: colors.textMuted, fontSize: fontSize.xs },
  footer: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  completedLabel: { flexDirection: 'row', alignItems: 'center', gap: 4 },
  completedLabelText: {
    color: colors.accent,
    fontSize: fontSize.sm,
    fontWeight: fontWeight.medium,
  },
  button: {
    backgroundColor: colors.accent,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.sm,
    borderRadius: radius.md,
    marginLeft: 'auto',
  },
  buttonCompleted: { backgroundColor: 'transparent', borderWidth: 1.5, borderColor: colors.accent },
  buttonText: { color: '#04110a', fontSize: fontSize.sm, fontWeight: fontWeight.bold },
  buttonTextCompleted: { color: colors.accent },
});

export default ClassCard;
