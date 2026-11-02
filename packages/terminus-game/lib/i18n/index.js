'use strict';

const es = require('./es');

const LANGUAGES = ['en', 'es'];
const ALIASES = {
  en: 'en',
  english: 'en',
  ingles: 'en',
  'inglés': 'en',
  es: 'es',
  spanish: 'es',
  espanol: 'es',
  'español': 'es'
};

function normalizeLanguage(value) {
  if (value === undefined || value === null || value === '') {
    return 'en';
  }
  const normalized = ALIASES[String(value).toLowerCase()];
  return normalized || null;
}

module.exports = {
  LANGUAGES,
  normalizeLanguage,
  es
};
