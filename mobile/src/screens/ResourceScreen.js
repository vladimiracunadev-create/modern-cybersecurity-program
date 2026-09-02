/**
 * ResourceScreen.js — recursos transversales completos y sin conexión.
 */

import React from 'react';
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
import { resourceById } from '../data/classes';
import { colors, spacing, radius, fontSize, fontWeight } from '../theme';

const openUrl = async (url, label) => {
  if (!url) return;
  try {
    if (await Linking.canOpenURL(url)) {
      await Linking.openURL(url);
      return;
    }
  } catch (error) {
    // cae al aviso visible
  }
  Alert.alert(
    `No se pudo abrir ${label}`,
    'Verifica que tengas conexión a internet y un navegador disponible.',
    [{ text: 'OK' }]
  );
};

export default function ResourceScreen({ route }) {
  const resource = resourceById(route.params?.resourceId);

  if (!resource) {
    return (
      <SafeAreaView style={styles.safeArea}>
        <View style={styles.missingCard}>
          <Text style={styles.title}>Recurso no disponible</Text>
          <Text style={styles.description}>Regenera el catálogo de la aplicación.</Text>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView
        style={styles.scroll}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        <View style={styles.headerCard}>
          <View style={styles.iconBadge}>
            <Text style={styles.icon}>{resource.icon}</Text>
          </View>
          <View style={styles.headerText}>
            <Text style={styles.eyebrow}>RECURSO TRANSVERSAL · OFFLINE</Text>
            <Text style={styles.title}>{resource.title}</Text>
            <Text style={styles.subtitle}>{resource.subtitle}</Text>
            <Text style={styles.description}>{resource.description}</Text>
          </View>
        </View>

        <View style={styles.notice}>
          <Text style={styles.noticeText}>
            Contenido educativo. No constituye asesoría legal; la ley aplicable depende de los
            hechos, la jurisdicción y la decisión de un tribunal.
          </Text>
        </View>

        <ClassContent
          blocks={resource.content}
          empty="El recurso no trae contenido embebido. Regenera el catálogo de la app."
        />
      </ScrollView>

      <View style={styles.bottomBar}>
        <TouchableOpacity
          style={styles.siteButton}
          onPress={() => openUrl(resource.siteUrl, 'el sitio')}
        >
          <Text style={styles.siteButtonText}>Ver en el sitio</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.githubButton}
          onPress={() => openUrl(resource.githubUrl, 'GitHub')}
        >
          <Text style={styles.githubButtonText}>GitHub</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: colors.bg },
  scroll: { flex: 1 },
  scrollContent: { padding: spacing.md, paddingBottom: spacing.xl },
  headerCard: {
    flexDirection: 'row',
    gap: spacing.md,
    backgroundColor: colors.bgCard,
    borderRadius: radius.lg,
    borderWidth: 1,
    borderColor: colors.warning,
    padding: spacing.md,
    marginBottom: spacing.md,
  },
  iconBadge: {
    width: 48,
    height: 48,
    borderRadius: radius.md,
    backgroundColor: '#33230a',
    alignItems: 'center',
    justifyContent: 'center',
  },
  icon: { fontSize: 24 },
  headerText: { flex: 1, minWidth: 0 },
  eyebrow: {
    color: colors.warning,
    fontSize: fontSize.xs,
    fontWeight: fontWeight.bold,
    marginBottom: 4,
  },
  title: { color: colors.text, fontSize: 22, fontWeight: fontWeight.bold, marginBottom: 4 },
  subtitle: { color: colors.warning, fontSize: fontSize.sm, lineHeight: 19, marginBottom: 8 },
  description: { color: colors.textMuted, fontSize: fontSize.sm, lineHeight: 20 },
  notice: {
    backgroundColor: colors.bgMuted,
    borderLeftWidth: 3,
    borderLeftColor: colors.warning,
    padding: spacing.md,
    borderRadius: radius.sm,
    marginBottom: spacing.sm,
  },
  noticeText: { color: colors.textMuted, fontSize: fontSize.sm, lineHeight: 20 },
  missingCard: { margin: spacing.md, padding: spacing.md, backgroundColor: colors.bgCard },
  bottomBar: {
    flexDirection: 'row',
    gap: spacing.sm,
    padding: spacing.md,
    backgroundColor: colors.bgCard,
    borderTopWidth: 1,
    borderTopColor: colors.border,
  },
  siteButton: {
    flex: 1.5,
    backgroundColor: colors.accent,
    borderRadius: radius.md,
    paddingVertical: 13,
    alignItems: 'center',
  },
  siteButtonText: { color: '#04110a', fontWeight: fontWeight.bold },
  githubButton: {
    flex: 1,
    borderWidth: 1,
    borderColor: colors.accentBlue,
    borderRadius: radius.md,
    paddingVertical: 13,
    alignItems: 'center',
  },
  githubButtonText: { color: colors.accentBlue, fontWeight: fontWeight.bold },
});
