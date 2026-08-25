/**
 * ClassContent.js — Pinta la clase completa embebida en el bundle.
 *
 * El generador (scripts/generar_curriculum_movil.py) convierte cada README en
 * una secuencia de bloques y la reparte en dos pestañas. Aquí solo se traduce
 * cada bloque a componentes de React Native:
 *
 *   h2 / h3 / h4 → jerarquía de títulos          li    → viñeta (o número) con sangría
 *   p            → párrafo                       code  → bloque monoespaciado
 *   q            → cita                          table → tabla con scroll horizontal
 *   dg           → el diagrama de la clase, como imagen empaquetada en el APK
 *
 * Un bloque de tipo desconocido se ignora en vez de romper la pantalla: si el
 * generador aprende a emitir uno nuevo, una app vieja sigue abriendo la clase.
 */

import React from 'react';
import { Image, ScrollView, StyleSheet, Text, View } from 'react-native';
import { diagramaPorId } from '../data/diagramas';
import { colors } from '../theme';

/**
 * Diagrama de la clase. La imagen viene empaquetada dentro del APK (no se
 * descarga) y se pinta a ancho completo respetando su proporción, que llega en
 * los datos: preguntarla en runtime con `Image.resolveAssetSource` funciona en
 * Android pero no existe en react-native-web, y reventaba la pantalla al abrir
 * una clase desde el navegador.
 *
 * Los diagramas se dibujan sobre fondo claro, así que llevan el suyo propio para
 * que se lean sobre el tema oscuro de la app.
 */
const Diagrama = ({ id }) => {
  const diagrama = diagramaPorId(id);
  if (!diagrama) {
    return (
      <View style={styles.diagram}>
        <Text style={styles.diagramText}>
          Diagrama de la clase — ábrela en el sitio para verlo.
        </Text>
      </View>
    );
  }
  // La proporción se aplica sobre una View, no sobre la Image: react-native-web
  // no respeta `aspectRatio` en una imagen y el diagrama salía estirado a su
  // alto natural.
  return (
    <View style={styles.diagramWrap}>
      <View style={{ width: '100%', aspectRatio: 1 / (diagrama.proporcion || 0.6) }}>
        <Image
          source={diagrama.fuente}
          style={styles.diagramImage}
          resizeMode="contain"
          accessibilityLabel="Diagrama de la clase"
        />
      </View>
    </View>
  );
};

const Bullet = ({ block }) => (
  <View style={[styles.liRow, block.d > 0 && { marginLeft: 16 * Math.min(block.d, 3) }]}>
    {block.n ? (
      <Text style={styles.liNumber}>{block.n}.</Text>
    ) : (
      <View style={[styles.liDot, block.d > 0 && styles.liDotNested]} />
    )}
    <Text style={styles.liText}>{block.x}</Text>
  </View>
);

const CodeBlock = ({ block }) => (
  <View style={styles.codeWrap}>
    {block.lang ? <Text style={styles.codeLang}>{block.lang}</Text> : null}
    <ScrollView horizontal showsHorizontalScrollIndicator={false}>
      <Text style={styles.codeText}>{block.x}</Text>
    </ScrollView>
  </View>
);

// Las tablas del curso llevan celdas largas ("Por qué importa"), así que se
// pintan con scroll horizontal y ancho fijo por columna en vez de comprimirlas
// hasta hacerlas ilegibles.
const Table = ({ block }) => {
  const cols = Math.max(block.h?.length ?? 0, ...(block.r ?? []).map((r) => r.length), 1);
  const width = cols <= 2 ? 200 : 160;
  return (
    <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.tableScroll}>
      <View style={styles.table}>
        {block.h?.length ? (
          <View style={[styles.tableRow, styles.tableHeadRow]}>
            {block.h.map((cell, i) => (
              <Text key={`h-${i}`} style={[styles.tableCell, styles.tableHeadCell, { width }]}>
                {cell}
              </Text>
            ))}
          </View>
        ) : null}
        {(block.r ?? []).map((row, ri) => (
          <View key={`r-${ri}`} style={styles.tableRow}>
            {row.map((cell, ci) => (
              <Text key={`c-${ri}-${ci}`} style={[styles.tableCell, { width }]}>
                {cell}
              </Text>
            ))}
          </View>
        ))}
      </View>
    </ScrollView>
  );
};

const Block = ({ block }) => {
  switch (block.t) {
    case 'h2':
      return <Text style={styles.h2}>{block.x}</Text>;
    case 'h3':
      return <Text style={styles.h3}>{block.x}</Text>;
    case 'h4':
      return <Text style={styles.h4}>{block.x}</Text>;
    case 'p':
      return <Text style={styles.p}>{block.x}</Text>;
    case 'li':
      return <Bullet block={block} />;
    case 'code':
      return <CodeBlock block={block} />;
    case 'table':
      return <Table block={block} />;
    case 'q':
      return (
        <View style={styles.quote}>
          <Text style={styles.quoteText}>{block.x}</Text>
        </View>
      );
    case 'dg':
      return <Diagrama id={block.img} />;
    default:
      return null;
  }
};

export default function ClassContent({ blocks, empty }) {
  if (!blocks || blocks.length === 0) {
    return (
      <View style={styles.emptyCard}>
        <Text style={styles.p}>{empty}</Text>
      </View>
    );
  }
  return (
    <View>
      {blocks.map((block, index) => (
        <Block key={`b-${index}`} block={block} />
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  h2: {
    color: colors.text,
    fontSize: 18,
    fontWeight: '800',
    marginTop: 22,
    marginBottom: 10,
    paddingBottom: 6,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  h3: { color: colors.accent, fontSize: 15, fontWeight: '700', marginTop: 16, marginBottom: 6 },
  h4: { color: colors.accentBlue, fontSize: 14, fontWeight: '700', marginTop: 12, marginBottom: 4 },
  p: { color: colors.textMuted, fontSize: 14, lineHeight: 22, marginBottom: 10 },
  liRow: { flexDirection: 'row', alignItems: 'flex-start', gap: 8, marginBottom: 7 },
  liDot: { width: 6, height: 6, borderRadius: 3, backgroundColor: colors.accent, marginTop: 8 },
  liDotNested: { backgroundColor: colors.accentBlue },
  liNumber: { color: colors.accent, fontSize: 13, fontWeight: '700', marginTop: 1, minWidth: 18 },
  liText: { flex: 1, minWidth: 0, color: colors.textMuted, fontSize: 14, lineHeight: 21 },
  codeWrap: {
    backgroundColor: colors.bgCode,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: colors.border,
    padding: 10,
    marginVertical: 10,
  },
  codeLang: {
    color: colors.accentBlue,
    fontSize: 10,
    fontWeight: '700',
    textTransform: 'uppercase',
    marginBottom: 6,
  },
  codeText: { color: colors.textCode, fontSize: 12, lineHeight: 18, fontFamily: 'monospace' },
  tableScroll: { marginVertical: 10 },
  table: { borderWidth: 1, borderColor: colors.border, borderRadius: 8, overflow: 'hidden' },
  tableRow: { flexDirection: 'row' },
  tableHeadRow: { backgroundColor: colors.bgMuted },
  tableCell: {
    color: colors.textMuted,
    fontSize: 12,
    lineHeight: 18,
    padding: 8,
    borderRightWidth: 1,
    borderTopWidth: 1,
    borderColor: colors.border,
  },
  tableHeadCell: { color: colors.text, fontWeight: '700', borderTopWidth: 0 },
  quote: {
    borderLeftWidth: 3,
    borderLeftColor: colors.accent,
    paddingLeft: 12,
    paddingVertical: 4,
    marginVertical: 10,
  },
  quoteText: { color: colors.textMuted, fontSize: 13, lineHeight: 21, fontStyle: 'italic' },
  diagramWrap: {
    backgroundColor: '#ffffff',
    borderRadius: 8,
    padding: 8,
    marginVertical: 12,
  },
  diagramImage: { width: '100%', height: '100%' },
  diagram: {
    backgroundColor: colors.bgMuted,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: colors.border,
    borderStyle: 'dashed',
    padding: 10,
    marginVertical: 10,
  },
  diagramText: { color: colors.textMuted, fontSize: 12, lineHeight: 18 },
  emptyCard: {
    backgroundColor: colors.bgCard,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: colors.border,
    padding: 14,
    marginBottom: 16,
  },
});
