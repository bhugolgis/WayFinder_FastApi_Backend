from typing import Optional
import datetime
import decimal
import uuid

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKeyConstraint, Integer, JSON, Numeric, PrimaryKeyConstraint, String, Text, UniqueConstraint, Uuid, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class DirectusActivity(Base):
    __tablename__ = 'directus_activity'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='directus_activity_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    action: Mapped[str] = mapped_column(String(45), nullable=False)
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    collection: Mapped[str] = mapped_column(String(64), nullable=False)
    item: Mapped[str] = mapped_column(String(255), nullable=False)
    user: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    ip: Mapped[Optional[str]] = mapped_column(String(50))
    user_agent: Mapped[Optional[str]] = mapped_column(Text)
    comment: Mapped[Optional[str]] = mapped_column(Text)
    origin: Mapped[Optional[str]] = mapped_column(String(255))

    directus_revisions: Mapped[list['DirectusRevisions']] = relationship('DirectusRevisions', back_populates='directus_activity')


class DirectusCollections(Base):
    __tablename__ = 'directus_collections'
    __table_args__ = (
        ForeignKeyConstraint(['group'], ['public.directus_collections.collection'], name='directus_collections_group_foreign'),
        PrimaryKeyConstraint('collection', name='directus_collections_pkey'),
        {'schema': 'public'}
    )

    collection: Mapped[str] = mapped_column(String(64), primary_key=True)
    hidden: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    singleton: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    archive_app_filter: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('true'))
    collapse: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("'open'::character varying"))
    versioning: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    icon: Mapped[Optional[str]] = mapped_column(String(30))
    note: Mapped[Optional[str]] = mapped_column(Text)
    display_template: Mapped[Optional[str]] = mapped_column(String(255))
    translations: Mapped[Optional[dict]] = mapped_column(JSON)
    archive_field: Mapped[Optional[str]] = mapped_column(String(64))
    archive_value: Mapped[Optional[str]] = mapped_column(String(255))
    unarchive_value: Mapped[Optional[str]] = mapped_column(String(255))
    sort_field: Mapped[Optional[str]] = mapped_column(String(64))
    accountability: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'all'::character varying"))
    color: Mapped[Optional[str]] = mapped_column(String(255))
    item_duplication_fields: Mapped[Optional[dict]] = mapped_column(JSON)
    sort: Mapped[Optional[int]] = mapped_column(Integer)
    group: Mapped[Optional[str]] = mapped_column(String(64))
    preview_url: Mapped[Optional[str]] = mapped_column(String(255))

    directus_collections: Mapped[Optional['DirectusCollections']] = relationship('DirectusCollections', remote_side=[collection], back_populates='directus_collections_reverse')
    directus_collections_reverse: Mapped[list['DirectusCollections']] = relationship('DirectusCollections', remote_side=[group], back_populates='directus_collections')
    directus_shares: Mapped[list['DirectusShares']] = relationship('DirectusShares', back_populates='directus_collections')
    directus_versions: Mapped[list['DirectusVersions']] = relationship('DirectusVersions', back_populates='directus_collections')


class DirectusExtensions(Base):
    __tablename__ = 'directus_extensions'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='directus_extensions_pkey'),
        {'schema': 'public'}
    )

    enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('true'))
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    folder: Mapped[str] = mapped_column(String(255), nullable=False)
    source: Mapped[str] = mapped_column(String(255), nullable=False)
    bundle: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)


class DirectusFields(Base):
    __tablename__ = 'directus_fields'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='directus_fields_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    collection: Mapped[str] = mapped_column(String(64), nullable=False)
    field: Mapped[str] = mapped_column(String(64), nullable=False)
    readonly: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    hidden: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    special: Mapped[Optional[str]] = mapped_column(String(64))
    interface: Mapped[Optional[str]] = mapped_column(String(64))
    options: Mapped[Optional[dict]] = mapped_column(JSON)
    display: Mapped[Optional[str]] = mapped_column(String(64))
    display_options: Mapped[Optional[dict]] = mapped_column(JSON)
    sort: Mapped[Optional[int]] = mapped_column(Integer)
    width: Mapped[Optional[str]] = mapped_column(String(30), server_default=text("'full'::character varying"))
    translations: Mapped[Optional[dict]] = mapped_column(JSON)
    note: Mapped[Optional[str]] = mapped_column(Text)
    conditions: Mapped[Optional[dict]] = mapped_column(JSON)
    required: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('false'))
    group: Mapped[Optional[str]] = mapped_column(String(64))
    validation: Mapped[Optional[dict]] = mapped_column(JSON)
    validation_message: Mapped[Optional[str]] = mapped_column(Text)


class DirectusFolders(Base):
    __tablename__ = 'directus_folders'
    __table_args__ = (
        ForeignKeyConstraint(['parent'], ['public.directus_folders.id'], name='directus_folders_parent_foreign'),
        PrimaryKeyConstraint('id', name='directus_folders_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    parent: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    directus_folders: Mapped[Optional['DirectusFolders']] = relationship('DirectusFolders', remote_side=[id], back_populates='directus_folders_reverse')
    directus_folders_reverse: Mapped[list['DirectusFolders']] = relationship('DirectusFolders', remote_side=[parent], back_populates='directus_folders')
    directus_files: Mapped[list['DirectusFiles']] = relationship('DirectusFiles', back_populates='directus_folders')
    directus_settings: Mapped[list['DirectusSettings']] = relationship('DirectusSettings', back_populates='directus_folders')


class DirectusMigrations(Base):
    __tablename__ = 'directus_migrations'
    __table_args__ = (
        PrimaryKeyConstraint('version', name='directus_migrations_pkey'),
        {'schema': 'public'}
    )

    version: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    timestamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('CURRENT_TIMESTAMP'))


class DirectusRelations(Base):
    __tablename__ = 'directus_relations'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='directus_relations_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    many_collection: Mapped[str] = mapped_column(String(64), nullable=False)
    many_field: Mapped[str] = mapped_column(String(64), nullable=False)
    one_deselect_action: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("'nullify'::character varying"))
    one_collection: Mapped[Optional[str]] = mapped_column(String(64))
    one_field: Mapped[Optional[str]] = mapped_column(String(64))
    one_collection_field: Mapped[Optional[str]] = mapped_column(String(64))
    one_allowed_collections: Mapped[Optional[str]] = mapped_column(Text)
    junction_field: Mapped[Optional[str]] = mapped_column(String(64))
    sort_field: Mapped[Optional[str]] = mapped_column(String(64))


class DirectusRoles(Base):
    __tablename__ = 'directus_roles'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='directus_roles_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    icon: Mapped[str] = mapped_column(String(30), nullable=False, server_default=text("'supervised_user_circle'::character varying"))
    enforce_tfa: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    admin_access: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    app_access: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('true'))
    description: Mapped[Optional[str]] = mapped_column(Text)
    ip_access: Mapped[Optional[str]] = mapped_column(Text)

    directus_permissions: Mapped[list['DirectusPermissions']] = relationship('DirectusPermissions', back_populates='directus_roles')
    directus_users: Mapped[list['DirectusUsers']] = relationship('DirectusUsers', back_populates='directus_roles')
    directus_presets: Mapped[list['DirectusPresets']] = relationship('DirectusPresets', back_populates='directus_roles')
    directus_shares: Mapped[list['DirectusShares']] = relationship('DirectusShares', back_populates='directus_roles')


class DirectusTranslations(Base):
    __tablename__ = 'directus_translations'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='directus_translations_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    language: Mapped[str] = mapped_column(String(255), nullable=False)
    key: Mapped[str] = mapped_column(String(255), nullable=False)
    value: Mapped[str] = mapped_column(Text, nullable=False)


class Test(Base):
    __tablename__ = 'test'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='test_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    RAM_Type: Mapped[Optional[str]] = mapped_column(String(255))


class DirectusPermissions(Base):
    __tablename__ = 'directus_permissions'
    __table_args__ = (
        ForeignKeyConstraint(['role'], ['public.directus_roles.id'], ondelete='CASCADE', name='directus_permissions_role_foreign'),
        PrimaryKeyConstraint('id', name='directus_permissions_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    collection: Mapped[str] = mapped_column(String(64), nullable=False)
    action: Mapped[str] = mapped_column(String(10), nullable=False)
    role: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    permissions: Mapped[Optional[dict]] = mapped_column(JSON)
    validation: Mapped[Optional[dict]] = mapped_column(JSON)
    presets: Mapped[Optional[dict]] = mapped_column(JSON)
    fields: Mapped[Optional[str]] = mapped_column(Text)

    directus_roles: Mapped[Optional['DirectusRoles']] = relationship('DirectusRoles', back_populates='directus_permissions')


class DirectusUsers(Base):
    __tablename__ = 'directus_users'
    __table_args__ = (
        ForeignKeyConstraint(['role'], ['public.directus_roles.id'], ondelete='SET NULL', name='directus_users_role_foreign'),
        PrimaryKeyConstraint('id', name='directus_users_pkey'),
        UniqueConstraint('email', name='directus_users_email_unique'),
        UniqueConstraint('external_identifier', name='directus_users_external_identifier_unique'),
        UniqueConstraint('token', name='directus_users_token_unique'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    status: Mapped[str] = mapped_column(String(16), nullable=False, server_default=text("'active'::character varying"))
    provider: Mapped[str] = mapped_column(String(128), nullable=False, server_default=text("'default'::character varying"))
    first_name: Mapped[Optional[str]] = mapped_column(String(50))
    last_name: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[Optional[str]] = mapped_column(String(128))
    password: Mapped[Optional[str]] = mapped_column(String(255))
    location: Mapped[Optional[str]] = mapped_column(String(255))
    title: Mapped[Optional[str]] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(Text)
    tags: Mapped[Optional[dict]] = mapped_column(JSON)
    avatar: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    language: Mapped[Optional[str]] = mapped_column(String(255), server_default=text('NULL::character varying'))
    tfa_secret: Mapped[Optional[str]] = mapped_column(String(255))
    role: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    token: Mapped[Optional[str]] = mapped_column(String(255))
    last_access: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    last_page: Mapped[Optional[str]] = mapped_column(String(255))
    external_identifier: Mapped[Optional[str]] = mapped_column(String(255))
    auth_data: Mapped[Optional[dict]] = mapped_column(JSON)
    email_notifications: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    appearance: Mapped[Optional[str]] = mapped_column(String(255))
    theme_dark: Mapped[Optional[str]] = mapped_column(String(255))
    theme_light: Mapped[Optional[str]] = mapped_column(String(255))
    theme_light_overrides: Mapped[Optional[dict]] = mapped_column(JSON)
    theme_dark_overrides: Mapped[Optional[dict]] = mapped_column(JSON)

    directus_roles: Mapped[Optional['DirectusRoles']] = relationship('DirectusRoles', back_populates='directus_users')
    Stations: Mapped[list['Stations']] = relationship('Stations', foreign_keys='[Stations.user_created]', back_populates='directus_users')
    Stations_: Mapped[list['Stations']] = relationship('Stations', foreign_keys='[Stations.user_updated]', back_populates='directus_users_')
    directus_dashboards: Mapped[list['DirectusDashboards']] = relationship('DirectusDashboards', back_populates='directus_users')
    directus_files: Mapped[list['DirectusFiles']] = relationship('DirectusFiles', foreign_keys='[DirectusFiles.modified_by]', back_populates='directus_users')
    directus_files_: Mapped[list['DirectusFiles']] = relationship('DirectusFiles', foreign_keys='[DirectusFiles.uploaded_by]', back_populates='directus_users_')
    directus_flows: Mapped[list['DirectusFlows']] = relationship('DirectusFlows', back_populates='directus_users')
    directus_notifications: Mapped[list['DirectusNotifications']] = relationship('DirectusNotifications', foreign_keys='[DirectusNotifications.recipient]', back_populates='directus_users')
    directus_notifications_: Mapped[list['DirectusNotifications']] = relationship('DirectusNotifications', foreign_keys='[DirectusNotifications.sender]', back_populates='directus_users_')
    directus_presets: Mapped[list['DirectusPresets']] = relationship('DirectusPresets', back_populates='directus_users')
    directus_shares: Mapped[list['DirectusShares']] = relationship('DirectusShares', back_populates='directus_users')
    directus_versions: Mapped[list['DirectusVersions']] = relationship('DirectusVersions', foreign_keys='[DirectusVersions.user_created]', back_populates='directus_users')
    directus_versions_: Mapped[list['DirectusVersions']] = relationship('DirectusVersions', foreign_keys='[DirectusVersions.user_updated]', back_populates='directus_users_')
    Places: Mapped[list['Places']] = relationship('Places', foreign_keys='[Places.user_created]', back_populates='directus_users')
    Places_: Mapped[list['Places']] = relationship('Places', foreign_keys='[Places.user_updated]', back_populates='directus_users_')
    directus_operations: Mapped[list['DirectusOperations']] = relationship('DirectusOperations', back_populates='directus_users')
    directus_panels: Mapped[list['DirectusPanels']] = relationship('DirectusPanels', back_populates='directus_users')
    directus_sessions: Mapped[list['DirectusSessions']] = relationship('DirectusSessions', back_populates='directus_users')


class Stations(Base):
    __tablename__ = 'Stations'
    __table_args__ = (
        ForeignKeyConstraint(['user_created'], ['public.directus_users.id'], name='stations_user_created_foreign'),
        ForeignKeyConstraint(['user_updated'], ['public.directus_users.id'], name='stations_user_updated_foreign'),
        PrimaryKeyConstraint('id', name='Stations_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'published'::character varying"))
    sort: Mapped[Optional[int]] = mapped_column(Integer)
    user_created: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    user_updated: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    date_updated: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    Station_Code: Mapped[Optional[str]] = mapped_column(String(255))
    Station_Name: Mapped[Optional[str]] = mapped_column(String(255))
    Station_Commercial_Name: Mapped[Optional[str]] = mapped_column(String(255))
    Station_Type: Mapped[Optional[str]] = mapped_column(String(255))
    Station_Latitude: Mapped[Optional[str]] = mapped_column(String(255))
    Station_Longitude: Mapped[Optional[str]] = mapped_column(String(255))
    Visitors_Count: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 0))
    Functional_Status: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'Non-functional'::character varying"))
    Display_Order: Mapped[Optional[int]] = mapped_column(Integer)
    Entry_Exit_Gates: Mapped[Optional[str]] = mapped_column(String(255))
    Lift_Status: Mapped[Optional[str]] = mapped_column(String(255))

    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', foreign_keys=[user_created], back_populates='Stations')
    directus_users_: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', foreign_keys=[user_updated], back_populates='Stations_')
    Places: Mapped[list['Places']] = relationship('Places', back_populates='Stations_')
    Visitor_Analysis: Mapped[list['VisitorAnalysis']] = relationship('VisitorAnalysis', back_populates='Stations_')


class DirectusDashboards(Base):
    __tablename__ = 'directus_dashboards'
    __table_args__ = (
        ForeignKeyConstraint(['user_created'], ['public.directus_users.id'], ondelete='SET NULL', name='directus_dashboards_user_created_foreign'),
        PrimaryKeyConstraint('id', name='directus_dashboards_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    icon: Mapped[str] = mapped_column(String(30), nullable=False, server_default=text("'dashboard'::character varying"))
    note: Mapped[Optional[str]] = mapped_column(Text)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('CURRENT_TIMESTAMP'))
    user_created: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    color: Mapped[Optional[str]] = mapped_column(String(255))

    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', back_populates='directus_dashboards')
    directus_panels: Mapped[list['DirectusPanels']] = relationship('DirectusPanels', back_populates='directus_dashboards')


class DirectusFiles(Base):
    __tablename__ = 'directus_files'
    __table_args__ = (
        ForeignKeyConstraint(['folder'], ['public.directus_folders.id'], ondelete='SET NULL', name='directus_files_folder_foreign'),
        ForeignKeyConstraint(['modified_by'], ['public.directus_users.id'], name='directus_files_modified_by_foreign'),
        ForeignKeyConstraint(['uploaded_by'], ['public.directus_users.id'], name='directus_files_uploaded_by_foreign'),
        PrimaryKeyConstraint('id', name='directus_files_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    storage: Mapped[str] = mapped_column(String(255), nullable=False)
    filename_download: Mapped[str] = mapped_column(String(255), nullable=False)
    uploaded_on: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    modified_on: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    filename_disk: Mapped[Optional[str]] = mapped_column(String(255))
    title: Mapped[Optional[str]] = mapped_column(String(255))
    type: Mapped[Optional[str]] = mapped_column(String(255))
    folder: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    uploaded_by: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    modified_by: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    charset: Mapped[Optional[str]] = mapped_column(String(50))
    filesize: Mapped[Optional[int]] = mapped_column(BigInteger)
    width: Mapped[Optional[int]] = mapped_column(Integer)
    height: Mapped[Optional[int]] = mapped_column(Integer)
    duration: Mapped[Optional[int]] = mapped_column(Integer)
    embed: Mapped[Optional[str]] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(Text)
    location: Mapped[Optional[str]] = mapped_column(Text)
    tags: Mapped[Optional[str]] = mapped_column(Text)
    metadata_: Mapped[Optional[dict]] = mapped_column('metadata', JSON)
    focal_point_x: Mapped[Optional[int]] = mapped_column(Integer)
    focal_point_y: Mapped[Optional[int]] = mapped_column(Integer)

    directus_folders: Mapped[Optional['DirectusFolders']] = relationship('DirectusFolders', back_populates='directus_files')
    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', foreign_keys=[modified_by], back_populates='directus_files')
    directus_users_: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', foreign_keys=[uploaded_by], back_populates='directus_files_')
    Places: Mapped[list['Places']] = relationship('Places', foreign_keys='[Places.Image]', back_populates='directus_files')
    Places_: Mapped[list['Places']] = relationship('Places', foreign_keys='[Places.SVG_Icon]', back_populates='directus_files_')
    Test_Places: Mapped[list['TestPlaces']] = relationship('TestPlaces', back_populates='directus_files')
    directus_settings: Mapped[list['DirectusSettings']] = relationship('DirectusSettings', foreign_keys='[DirectusSettings.project_logo]', back_populates='directus_files')
    directus_settings_: Mapped[list['DirectusSettings']] = relationship('DirectusSettings', foreign_keys='[DirectusSettings.public_background]', back_populates='directus_files_')
    directus_settings1: Mapped[list['DirectusSettings']] = relationship('DirectusSettings', foreign_keys='[DirectusSettings.public_favicon]', back_populates='directus_files1')
    directus_settings2: Mapped[list['DirectusSettings']] = relationship('DirectusSettings', foreign_keys='[DirectusSettings.public_foreground]', back_populates='directus_files2')


class DirectusFlows(Base):
    __tablename__ = 'directus_flows'
    __table_args__ = (
        ForeignKeyConstraint(['user_created'], ['public.directus_users.id'], ondelete='SET NULL', name='directus_flows_user_created_foreign'),
        PrimaryKeyConstraint('id', name='directus_flows_pkey'),
        UniqueConstraint('operation', name='directus_flows_operation_unique'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("'active'::character varying"))
    icon: Mapped[Optional[str]] = mapped_column(String(30))
    color: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    trigger: Mapped[Optional[str]] = mapped_column(String(255))
    accountability: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'all'::character varying"))
    options: Mapped[Optional[dict]] = mapped_column(JSON)
    operation: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('CURRENT_TIMESTAMP'))
    user_created: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', back_populates='directus_flows')
    directus_operations: Mapped[list['DirectusOperations']] = relationship('DirectusOperations', back_populates='directus_flows')
    directus_webhooks: Mapped[list['DirectusWebhooks']] = relationship('DirectusWebhooks', back_populates='directus_flows')


class DirectusNotifications(Base):
    __tablename__ = 'directus_notifications'
    __table_args__ = (
        ForeignKeyConstraint(['recipient'], ['public.directus_users.id'], ondelete='CASCADE', name='directus_notifications_recipient_foreign'),
        ForeignKeyConstraint(['sender'], ['public.directus_users.id'], name='directus_notifications_sender_foreign'),
        PrimaryKeyConstraint('id', name='directus_notifications_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    recipient: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    subject: Mapped[str] = mapped_column(String(255), nullable=False)
    timestamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('CURRENT_TIMESTAMP'))
    status: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'inbox'::character varying"))
    sender: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    message: Mapped[Optional[str]] = mapped_column(Text)
    collection: Mapped[Optional[str]] = mapped_column(String(64))
    item: Mapped[Optional[str]] = mapped_column(String(255))

    directus_users: Mapped['DirectusUsers'] = relationship('DirectusUsers', foreign_keys=[recipient], back_populates='directus_notifications')
    directus_users_: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', foreign_keys=[sender], back_populates='directus_notifications_')


class DirectusPresets(Base):
    __tablename__ = 'directus_presets'
    __table_args__ = (
        ForeignKeyConstraint(['role'], ['public.directus_roles.id'], ondelete='CASCADE', name='directus_presets_role_foreign'),
        ForeignKeyConstraint(['user'], ['public.directus_users.id'], ondelete='CASCADE', name='directus_presets_user_foreign'),
        PrimaryKeyConstraint('id', name='directus_presets_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bookmark: Mapped[Optional[str]] = mapped_column(String(255))
    user: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    role: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    collection: Mapped[Optional[str]] = mapped_column(String(64))
    search: Mapped[Optional[str]] = mapped_column(String(100))
    layout: Mapped[Optional[str]] = mapped_column(String(100), server_default=text("'tabular'::character varying"))
    layout_query: Mapped[Optional[dict]] = mapped_column(JSON)
    layout_options: Mapped[Optional[dict]] = mapped_column(JSON)
    refresh_interval: Mapped[Optional[int]] = mapped_column(Integer)
    filter: Mapped[Optional[dict]] = mapped_column(JSON)
    icon: Mapped[Optional[str]] = mapped_column(String(30), server_default=text("'bookmark'::character varying"))
    color: Mapped[Optional[str]] = mapped_column(String(255))

    directus_roles: Mapped[Optional['DirectusRoles']] = relationship('DirectusRoles', back_populates='directus_presets')
    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', back_populates='directus_presets')


class DirectusShares(Base):
    __tablename__ = 'directus_shares'
    __table_args__ = (
        ForeignKeyConstraint(['collection'], ['public.directus_collections.collection'], ondelete='CASCADE', name='directus_shares_collection_foreign'),
        ForeignKeyConstraint(['role'], ['public.directus_roles.id'], ondelete='CASCADE', name='directus_shares_role_foreign'),
        ForeignKeyConstraint(['user_created'], ['public.directus_users.id'], ondelete='SET NULL', name='directus_shares_user_created_foreign'),
        PrimaryKeyConstraint('id', name='directus_shares_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    collection: Mapped[str] = mapped_column(String(64), nullable=False)
    item: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    role: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    password: Mapped[Optional[str]] = mapped_column(String(255))
    user_created: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('CURRENT_TIMESTAMP'))
    date_start: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    date_end: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    times_used: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    max_uses: Mapped[Optional[int]] = mapped_column(Integer)

    directus_collections: Mapped['DirectusCollections'] = relationship('DirectusCollections', back_populates='directus_shares')
    directus_roles: Mapped[Optional['DirectusRoles']] = relationship('DirectusRoles', back_populates='directus_shares')
    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', back_populates='directus_shares')
    directus_sessions: Mapped[list['DirectusSessions']] = relationship('DirectusSessions', back_populates='directus_shares')


class DirectusVersions(Base):
    __tablename__ = 'directus_versions'
    __table_args__ = (
        ForeignKeyConstraint(['collection'], ['public.directus_collections.collection'], ondelete='CASCADE', name='directus_versions_collection_foreign'),
        ForeignKeyConstraint(['user_created'], ['public.directus_users.id'], ondelete='SET NULL', name='directus_versions_user_created_foreign'),
        ForeignKeyConstraint(['user_updated'], ['public.directus_users.id'], name='directus_versions_user_updated_foreign'),
        PrimaryKeyConstraint('id', name='directus_versions_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    key: Mapped[str] = mapped_column(String(64), nullable=False)
    collection: Mapped[str] = mapped_column(String(64), nullable=False)
    item: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    hash: Mapped[Optional[str]] = mapped_column(String(255))
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('CURRENT_TIMESTAMP'))
    date_updated: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('CURRENT_TIMESTAMP'))
    user_created: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    user_updated: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    directus_collections: Mapped['DirectusCollections'] = relationship('DirectusCollections', back_populates='directus_versions')
    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', foreign_keys=[user_created], back_populates='directus_versions')
    directus_users_: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', foreign_keys=[user_updated], back_populates='directus_versions_')
    directus_revisions: Mapped[list['DirectusRevisions']] = relationship('DirectusRevisions', back_populates='directus_versions')


class Places(Base):
    __tablename__ = 'Places'
    __table_args__ = (
        ForeignKeyConstraint(['Image'], ['public.directus_files.id'], ondelete='SET NULL', name='places_image_foreign'),
        ForeignKeyConstraint(['SVG_Icon'], ['public.directus_files.id'], ondelete='SET NULL', name='places_svg_icon_foreign'),
        ForeignKeyConstraint(['Station'], ['public.Stations.id'], ondelete='SET NULL', name='places_station_foreign'),
        ForeignKeyConstraint(['user_created'], ['public.directus_users.id'], name='places_user_created_foreign'),
        ForeignKeyConstraint(['user_updated'], ['public.directus_users.id'], name='places_user_updated_foreign'),
        PrimaryKeyConstraint('id', name='Places_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'published'::character varying"))
    sort: Mapped[Optional[int]] = mapped_column(Integer)
    user_created: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    user_updated: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    date_updated: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    Station: Mapped[Optional[int]] = mapped_column(Integer)
    Locality_Name: Mapped[Optional[str]] = mapped_column(String(255), server_default=text('NULL::character varying'))
    Type_of_Locality: Mapped[Optional[str]] = mapped_column(String(255))
    Sub_Type_of_Locality: Mapped[Optional[str]] = mapped_column(String(255))
    Latitude: Mapped[Optional[str]] = mapped_column(String(255))
    Longitude: Mapped[Optional[str]] = mapped_column(String(255))
    Nearest_Gates: Mapped[Optional[str]] = mapped_column(String(255))
    Distance_From_Nearest_Gate: Mapped[Optional[str]] = mapped_column(String(255))
    SVG_Icon: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    Image: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    Bus_Stops: Mapped[Optional[str]] = mapped_column(String(255))

    directus_files: Mapped[Optional['DirectusFiles']] = relationship('DirectusFiles', foreign_keys=[Image], back_populates='Places')
    directus_files_: Mapped[Optional['DirectusFiles']] = relationship('DirectusFiles', foreign_keys=[SVG_Icon], back_populates='Places_')
    Stations_: Mapped[Optional['Stations']] = relationship('Stations', back_populates='Places')
    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', foreign_keys=[user_created], back_populates='Places')
    directus_users_: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', foreign_keys=[user_updated], back_populates='Places_')
    Visitor_Analysis: Mapped[list['VisitorAnalysis']] = relationship('VisitorAnalysis', back_populates='Places_')


class TestPlaces(Base):
    __tablename__ = 'Test_Places'
    __table_args__ = (
        ForeignKeyConstraint(['image'], ['public.directus_files.id'], ondelete='SET NULL', name='test_places_image_foreign'),
        PrimaryKeyConstraint('id', name='Test_Places_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Locality_N: Mapped[Optional[str]] = mapped_column(String(255))
    Type_of_Lo: Mapped[Optional[str]] = mapped_column(String(255))
    status: Mapped[Optional[str]] = mapped_column(String(255))
    Sub_Type_o: Mapped[Optional[str]] = mapped_column(String(255))
    sort: Mapped[Optional[int]] = mapped_column(Integer)
    Latitude: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 5))
    Longitude: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 5))
    Station_St: Mapped[Optional[str]] = mapped_column(String(255))
    Nearest_Gates: Mapped[Optional[str]] = mapped_column(String(255))
    image: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    directus_files: Mapped[Optional['DirectusFiles']] = relationship('DirectusFiles', back_populates='Test_Places')


class DirectusOperations(Base):
    __tablename__ = 'directus_operations'
    __table_args__ = (
        ForeignKeyConstraint(['flow'], ['public.directus_flows.id'], ondelete='CASCADE', name='directus_operations_flow_foreign'),
        ForeignKeyConstraint(['reject'], ['public.directus_operations.id'], name='directus_operations_reject_foreign'),
        ForeignKeyConstraint(['resolve'], ['public.directus_operations.id'], name='directus_operations_resolve_foreign'),
        ForeignKeyConstraint(['user_created'], ['public.directus_users.id'], ondelete='SET NULL', name='directus_operations_user_created_foreign'),
        PrimaryKeyConstraint('id', name='directus_operations_pkey'),
        UniqueConstraint('reject', name='directus_operations_reject_unique'),
        UniqueConstraint('resolve', name='directus_operations_resolve_unique'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    key: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[str] = mapped_column(String(255), nullable=False)
    position_x: Mapped[int] = mapped_column(Integer, nullable=False)
    position_y: Mapped[int] = mapped_column(Integer, nullable=False)
    flow: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    options: Mapped[Optional[dict]] = mapped_column(JSON)
    resolve: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    reject: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('CURRENT_TIMESTAMP'))
    user_created: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    directus_flows: Mapped['DirectusFlows'] = relationship('DirectusFlows', back_populates='directus_operations')
    directus_operations: Mapped[Optional['DirectusOperations']] = relationship('DirectusOperations', uselist=False, remote_side=[id], foreign_keys=[reject], back_populates='directus_operations_reverse')
    directus_operations_reverse: Mapped[Optional['DirectusOperations']] = relationship('DirectusOperations', uselist=False, remote_side=[reject], foreign_keys=[reject], back_populates='directus_operations')
    directus_operations_: Mapped[Optional['DirectusOperations']] = relationship('DirectusOperations', uselist=False, remote_side=[id], foreign_keys=[resolve], back_populates='directus_operations__reverse')
    directus_operations__reverse: Mapped[Optional['DirectusOperations']] = relationship('DirectusOperations', uselist=False, remote_side=[resolve], foreign_keys=[resolve], back_populates='directus_operations_')
    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', back_populates='directus_operations')


class DirectusPanels(Base):
    __tablename__ = 'directus_panels'
    __table_args__ = (
        ForeignKeyConstraint(['dashboard'], ['public.directus_dashboards.id'], ondelete='CASCADE', name='directus_panels_dashboard_foreign'),
        ForeignKeyConstraint(['user_created'], ['public.directus_users.id'], ondelete='SET NULL', name='directus_panels_user_created_foreign'),
        PrimaryKeyConstraint('id', name='directus_panels_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    dashboard: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    show_header: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    type: Mapped[str] = mapped_column(String(255), nullable=False)
    position_x: Mapped[int] = mapped_column(Integer, nullable=False)
    position_y: Mapped[int] = mapped_column(Integer, nullable=False)
    width: Mapped[int] = mapped_column(Integer, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    icon: Mapped[Optional[str]] = mapped_column(String(30), server_default=text('NULL::character varying'))
    color: Mapped[Optional[str]] = mapped_column(String(10))
    note: Mapped[Optional[str]] = mapped_column(Text)
    options: Mapped[Optional[dict]] = mapped_column(JSON)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=text('CURRENT_TIMESTAMP'))
    user_created: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    directus_dashboards: Mapped['DirectusDashboards'] = relationship('DirectusDashboards', back_populates='directus_panels')
    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', back_populates='directus_panels')


class DirectusRevisions(Base):
    __tablename__ = 'directus_revisions'
    __table_args__ = (
        ForeignKeyConstraint(['activity'], ['public.directus_activity.id'], ondelete='CASCADE', name='directus_revisions_activity_foreign'),
        ForeignKeyConstraint(['parent'], ['public.directus_revisions.id'], name='directus_revisions_parent_foreign'),
        ForeignKeyConstraint(['version'], ['public.directus_versions.id'], ondelete='CASCADE', name='directus_revisions_version_foreign'),
        PrimaryKeyConstraint('id', name='directus_revisions_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    activity: Mapped[int] = mapped_column(Integer, nullable=False)
    collection: Mapped[str] = mapped_column(String(64), nullable=False)
    item: Mapped[str] = mapped_column(String(255), nullable=False)
    data: Mapped[Optional[dict]] = mapped_column(JSON)
    delta: Mapped[Optional[dict]] = mapped_column(JSON)
    parent: Mapped[Optional[int]] = mapped_column(Integer)
    version: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    directus_activity: Mapped['DirectusActivity'] = relationship('DirectusActivity', back_populates='directus_revisions')
    directus_revisions: Mapped[Optional['DirectusRevisions']] = relationship('DirectusRevisions', remote_side=[id], back_populates='directus_revisions_reverse')
    directus_revisions_reverse: Mapped[list['DirectusRevisions']] = relationship('DirectusRevisions', remote_side=[parent], back_populates='directus_revisions')
    directus_versions: Mapped[Optional['DirectusVersions']] = relationship('DirectusVersions', back_populates='directus_revisions')


class DirectusSessions(Base):
    __tablename__ = 'directus_sessions'
    __table_args__ = (
        ForeignKeyConstraint(['share'], ['public.directus_shares.id'], ondelete='CASCADE', name='directus_sessions_share_foreign'),
        ForeignKeyConstraint(['user'], ['public.directus_users.id'], ondelete='CASCADE', name='directus_sessions_user_foreign'),
        PrimaryKeyConstraint('token', name='directus_sessions_pkey'),
        {'schema': 'public'}
    )

    token: Mapped[str] = mapped_column(String(64), primary_key=True)
    expires: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False)
    user: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    ip: Mapped[Optional[str]] = mapped_column(String(255))
    user_agent: Mapped[Optional[str]] = mapped_column(Text)
    share: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    origin: Mapped[Optional[str]] = mapped_column(String(255))

    directus_shares: Mapped[Optional['DirectusShares']] = relationship('DirectusShares', back_populates='directus_sessions')
    directus_users: Mapped[Optional['DirectusUsers']] = relationship('DirectusUsers', back_populates='directus_sessions')


class DirectusSettings(Base):
    __tablename__ = 'directus_settings'
    __table_args__ = (
        ForeignKeyConstraint(['project_logo'], ['public.directus_files.id'], name='directus_settings_project_logo_foreign'),
        ForeignKeyConstraint(['public_background'], ['public.directus_files.id'], name='directus_settings_public_background_foreign'),
        ForeignKeyConstraint(['public_favicon'], ['public.directus_files.id'], name='directus_settings_public_favicon_foreign'),
        ForeignKeyConstraint(['public_foreground'], ['public.directus_files.id'], name='directus_settings_public_foreground_foreign'),
        ForeignKeyConstraint(['storage_default_folder'], ['public.directus_folders.id'], ondelete='SET NULL', name='directus_settings_storage_default_folder_foreign'),
        PrimaryKeyConstraint('id', name='directus_settings_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_name: Mapped[str] = mapped_column(String(100), nullable=False, server_default=text("'Directus'::character varying"))
    project_color: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("'#6644FF'::character varying"))
    default_language: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("'en-US'::character varying"))
    default_appearance: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("'auto'::character varying"))
    project_url: Mapped[Optional[str]] = mapped_column(String(255))
    project_logo: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    public_foreground: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    public_background: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    public_note: Mapped[Optional[str]] = mapped_column(Text)
    auth_login_attempts: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('25'))
    auth_password_policy: Mapped[Optional[str]] = mapped_column(String(100))
    storage_asset_transform: Mapped[Optional[str]] = mapped_column(String(7), server_default=text("'all'::character varying"))
    storage_asset_presets: Mapped[Optional[dict]] = mapped_column(JSON)
    custom_css: Mapped[Optional[str]] = mapped_column(Text)
    storage_default_folder: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    basemaps: Mapped[Optional[dict]] = mapped_column(JSON)
    mapbox_key: Mapped[Optional[str]] = mapped_column(String(255))
    module_bar: Mapped[Optional[dict]] = mapped_column(JSON)
    project_descriptor: Mapped[Optional[str]] = mapped_column(String(100))
    custom_aspect_ratios: Mapped[Optional[dict]] = mapped_column(JSON)
    public_favicon: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    default_theme_light: Mapped[Optional[str]] = mapped_column(String(255))
    theme_light_overrides: Mapped[Optional[dict]] = mapped_column(JSON)
    default_theme_dark: Mapped[Optional[str]] = mapped_column(String(255))
    theme_dark_overrides: Mapped[Optional[dict]] = mapped_column(JSON)
    report_error_url: Mapped[Optional[str]] = mapped_column(String(255))
    report_bug_url: Mapped[Optional[str]] = mapped_column(String(255))
    report_feature_url: Mapped[Optional[str]] = mapped_column(String(255))

    directus_files: Mapped[Optional['DirectusFiles']] = relationship('DirectusFiles', foreign_keys=[project_logo], back_populates='directus_settings')
    directus_files_: Mapped[Optional['DirectusFiles']] = relationship('DirectusFiles', foreign_keys=[public_background], back_populates='directus_settings_')
    directus_files1: Mapped[Optional['DirectusFiles']] = relationship('DirectusFiles', foreign_keys=[public_favicon], back_populates='directus_settings1')
    directus_files2: Mapped[Optional['DirectusFiles']] = relationship('DirectusFiles', foreign_keys=[public_foreground], back_populates='directus_settings2')
    directus_folders: Mapped[Optional['DirectusFolders']] = relationship('DirectusFolders', back_populates='directus_settings')


class DirectusWebhooks(Base):
    __tablename__ = 'directus_webhooks'
    __table_args__ = (
        ForeignKeyConstraint(['migrated_flow'], ['public.directus_flows.id'], ondelete='SET NULL', name='directus_webhooks_migrated_flow_foreign'),
        PrimaryKeyConstraint('id', name='directus_webhooks_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    method: Mapped[str] = mapped_column(String(10), nullable=False, server_default=text("'POST'::character varying"))
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(10), nullable=False, server_default=text("'active'::character varying"))
    data: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('true'))
    actions: Mapped[str] = mapped_column(String(100), nullable=False)
    collections: Mapped[str] = mapped_column(String(255), nullable=False)
    was_active_before_deprecation: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    headers: Mapped[Optional[dict]] = mapped_column(JSON)
    migrated_flow: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    directus_flows: Mapped[Optional['DirectusFlows']] = relationship('DirectusFlows', back_populates='directus_webhooks')


class VisitorAnalysis(Base):
    __tablename__ = 'Visitor_Analysis'
    __table_args__ = (
        ForeignKeyConstraint(['Place'], ['public.Places.id'], ondelete='SET NULL', name='visitor_analysis_place_foreign'),
        ForeignKeyConstraint(['Station'], ['public.Stations.id'], ondelete='SET NULL', name='visitor_analysis_station_foreign'),
        PrimaryKeyConstraint('id', name='Visitor_Analysis_pkey'),
        {'schema': 'public'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sort: Mapped[Optional[int]] = mapped_column(Integer)
    date_created: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    Station: Mapped[Optional[int]] = mapped_column(Integer)
    Place: Mapped[Optional[int]] = mapped_column(Integer)
    Username: Mapped[Optional[str]] = mapped_column(String(255))

    Places_: Mapped[Optional['Places']] = relationship('Places', back_populates='Visitor_Analysis')
    Stations_: Mapped[Optional['Stations']] = relationship('Stations', back_populates='Visitor_Analysis')