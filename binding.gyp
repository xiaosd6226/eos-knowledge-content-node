{
  'targets': [
    {
      'target_name': 'ekn-bindings',
      'sources': [
        'src/gi.cc',
        'src/value.cc',
        'src/function.cc',
        'src/gobject.cc',
        'src/closure.cc',
        'src/boxed.cc',
      ],
      'cflags': [
        '<!@(pkg-config --cflags gobject-introspection-1.0 eos-knowledge-content-0)'
      ],
      'ldflags': [
        '<!@(pkg-config --libs-only-L --libs-only-other gobject-introspection-1.0 eos-knowledge-content-0)',
      ],
      'libraries': [
        '<!@(pkg-config --libs-only-l gobject-introspection-1.0 eos-knowledge-content-0)',
      ],
    },
  ],
}
